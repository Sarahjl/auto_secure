import matplotlib.pyplot as plt

def plot_histograms(df):
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 2, 1)
    df['idade'].hist(bins=15)
    plt.title("Distribuição de idade")

    plt.subplot(1, 2, 2)
    df['renda'].hist(bins=15)
    plt.title("Distribuição de renda")

    plt.tight_layout()
    plt.show()
