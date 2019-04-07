
def neteasy_music(duration):
	time = 0
	while time <= duration:
		print("music to %d"%time)
		time += 1

def youku_movie(duration):
	time = 0
	while time <= duration:
		print("Movie to %d"%time)
		time += 1


def main():
	neteasy_music(10)
	youku_movie(20)

if __name__ == '__main__':
	main()

