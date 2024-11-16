
import tkinter as tk
from models import RegressionModel, DigitClassificationModel, LanguageIDModel
from dataset import Dataset

class InteractiveTrainingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Interactive Model Training")

        self.learning_rate = tk.DoubleVar(value=-0.01)
        self.model_type = tk.StringVar(value="RegressionModel")

        tk.Label(master, text="Learning Rate:").grid(row=0, column=0)
        tk.Entry(master, textvariable=self.learning_rate).grid(row=0, column=1)

        tk.Label(master, text="Model Type:").grid(row=1, column=0)
        tk.OptionMenu(master, self.model_type, "RegressionModel", "DigitClassificationModel", "LanguageIDModel").grid(row=1, column=1)

        self.train_button = tk.Button(master, text="Train", command=self.train_model)
        self.train_button.grid(row=2, column=0, columnspan=2)

        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.grid(row=3, column=0, columnspan=2)

    def train_model(self):
        model_class = globals()[self.model_type.get()]
        model = model_class()
        dataset = Dataset()  # Cargar tu dataset aquí

        learning_rate = self.learning_rate.get()
        self.output_text.insert(tk.END, f"Training {self.model_type.get()} with learning rate {learning_rate}\n")

        while True:
            total_loss = 0
            for x, y in dataset.iterate_once(100):
                loss = model.get_loss(x, y)
                total_loss += nn.as_scalar(loss)
                grad_w1, grad_b1, grad_w2, grad_b2 = nn.gradients(loss, [model.w1, model.b1, model.w2, model.b2])
                model.w1.update(grad_w1, learning_rate)
                model.b1.update(grad_b1, learning_rate)
                model.w2.update(grad_w2, learning_rate)
                model.b2.update(grad_b2, learning_rate)
            self.output_text.insert(tk.END, f"Total Loss: {total_loss}\n")
            self.master.update()
            if total_loss < 0.1:
                break

if __name__ == "__main__":
    root = tk.Tk()
    app = InteractiveTrainingApp(root)
    root.mainloop()