import matplotlib.pyplot as plt

def count(num, df):
    return list(df['2D']).count(num)


def cal_prob(numer, deno):
    smooth = 0.001
    res = numer/(deno+0.001)
    return res


def joint_count(a, b, df):
    count = 0
    for i in range(len(df)-1):
        if (df['2D'][i] == a and df['2D'][i+1] == b):
            count += 1
    return count


def conditional_prob(a, b, df):
    # P(b|a)
    a_count = count(a, df)
    ab_count = joint_count(a, b, df)
    return cal_prob(ab_count, a_count)


class Mat_2D:
    ### Getter and Setter
    def __init__(self, df, width, n_top_prob, n_top_weight):
        self.df = df
        self.width = width
        self.init_prob = self.set_init_prob()
        self.transition_mat = self.set_transition_matrix()
        self.n_top_prob = n_top_prob
        self.n_top_weight = n_top_weight

    def set_init_prob(self):
        init_prob = []
        for i in range(self.width):
            numer = count(i, self.df)
            init_prob.append(cal_prob(numer, len(self.df)))
        return init_prob

    def set_transition_matrix(self):
        transition_mat = []
        for r in range(self.width):
            temp = []
            for c in range(self.width):
                temp.append(conditional_prob(r, c, self.df))
            transition_mat.append(temp)
        return transition_mat

    def get_init_prob(self, v):
        return self.init_prob[v]

    def get_transition_prob(self, r, c):
        return self.transition_mat[r][c]
    # End Getter and Setter

    # Prediction Function
    def pred_row(self, trans):
        prob = []
        X = 1
        X *= self.get_init_prob(trans[0])
        for i in range(1, len(trans)):
            temp = self.get_transition_prob(trans[i-1], trans[i])
            X *= temp
        for j in range(self.width):
            temp = self.get_transition_prob(trans[-1], j)
            prob.append(X * temp)
        prob_dict = dict(zip(range(self.width), prob))
        sorted_prob = dict(
            sorted(prob_dict.items(), key=lambda x: x[1], reverse=True))
        out = dict(list(sorted_prob.items())[0:self.n_top_prob])
        return out

    def predict(self, df, trans_no):
        predicted = df.copy()
        temp = []
        for n in range(trans_no-1):
            temp.append(None)
        for i in range(trans_no-1, len(df['2D'])):
            pred = list(self.pred_row([df['2D'].iloc[i-t]
                                  for t in range(trans_no)]).keys())
            temp.append(pred)
        predicted["y"] = temp
        return predicted

    def accuracy_row(self, act, pred):
        ind = len(pred)
        if act in pred:
            ind = pred.index(act)
        return self.n_top_weight[ind]

    def accuracy(self, act_ser, pred_ser, trans_no):
        act_list = list(act_ser)[trans_no:]
        pred_list = list(pred_ser)[(trans_no-1):-1]
        sum_prob = 0
        size = len(pred_list)
        for i in range(size):
            sum_prob += self.accuracy_row(act_list[i], pred_list[i])
        acc = sum_prob/size
        return acc
    # End Prediction Function

    # Visualization
    def viz(self, x_list, y_list, xlabel, ylabel, title):
        fig = plt.figure(figsize = (20, 5)) 
        # creating the bar plot
        plt.bar(x_list, y_list, color ='maroon', width = 0.8)        
        plt.xlabel(xlabel,fontsize=26)
        plt.ylabel(ylabel,fontsize=26)
        plt.title(title,fontsize=28)
        for i in range(len(y_list)):
            plt.text(x_list[i]-0.25, y_list[i]+0.007, y_list[i],fontsize=24)
        plt.show()

    def acc_viz(self, df):
        accuracies = []
        for tran in range(1, 11):
            pred = self.predict(df, tran)
            acc = self.accuracy(pred['2D'], pred['y'], tran)
            accuracies.append(round(acc, 2))
        self.viz(list(range(1,11)), accuracies, 'No. of Transition', 'Accuracy', 'Accuracies of each Transition')
    # End Visualization
# End Class Mat_2D