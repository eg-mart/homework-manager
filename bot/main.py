from threading import Thread
import vk_frontend


if __name__ == '__main__':
    vk = Thread(target=vk_frontend.run)
    vk.start()
    vk.join()

