import pickle
import os


def input_scores():
    scores = []
    while True:
        score = int(input("#{}? ".format(len(scores) + 1)))
        if score < 0:
            break
        scores.append(score)
    return scores


def get_average(scores):
    return round(sum(scores) / len(scores), 1)


def show_scores(scores):
    print("개인점수:", ' '.join(map(str, scores)))
    print("평균:", get_average(scores))


def save_scores(scores):
    with open("score.bin", "wb") as f:
        pickle.dump(scores, f)


def load_scores():
    if os.path.exists("score.bin"):
        with open("score.bin", "rb") as f:
            scores = pickle.load(f)
        return scores
    return None


def main():
    scores = load_scores()
    if scores is None:
        print("[점수 입력]")
        scores = input_scores()
        save_scores(scores)
    else:
        print("[파일읽기]")
    print("[점수 출력]")
    show_scores(scores)


if __name__ == "__main__":
    main()