import matplotlib.pyplot as plt
import matplotlib.animation as animation

import sample


def plot_artist_animation():
    fig = plt.figure()

    ims = []

    for i in range(10):
        sample_data = sample.get_sample_data()
        x_l = sample_data[0]
        y_l = sample_data[1]
        im = plt.plot(x_l, y_l)
        ims.append(im)                  # グラフを配列 ims に追加

    # 10枚のプロットを 100ms ごとに表示
    ani = animation.ArtistAnimation(fig, ims, interval=100)
    plt.show()
    ani.save("anime.gif", writer="pillow")



def main():

    # artist 先に配列を用意する
    plot_artist_animation()



if __name__ == '__main__':
    main()