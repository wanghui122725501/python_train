
def neteasy_music(duration):
	time = 0
	while time <= duration:
		print("music to %d"%time)
		time += 1
		yield None
	raise StopIteration()

def youku_movie(duration):
	time = 0
	while time <= duration:
		print("Movie to %d"%time)
		time += 1
		yield None
	raise StopIteration()

def main():
	music_iter = neteasy_music(10)
	movie_iter = youku_movie(20)
	music_stop = False
	movie_stop = False
	while True:
		try:
			next(music_iter)
		except StopIteration:
			print('音乐播放完毕')
			music_stop = True
		try:
			next(movie_iter)	
		except StopIteration:
			print('电影播放播放完毕')
			movie_stop = True

		if music_stop and movie_stop:
			break		

if __name__ == '__main__':
	main()