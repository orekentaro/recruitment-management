class Constance:
    AUTH_ADMIN = "admin"
    AUTH_STAFF = "staff"
    AUTH = (
        (AUTH_ADMIN, "管理者権限"),
        (AUTH_STAFF, "スタッフ権限"),
    )

    GENDER_MEN = "men"
    GENDER_WOMAN = "woman"
    GENDER_UNKNOWN = "unknown"

    GENDER = (
        (GENDER_MEN, "男性"),
        (GENDER_WOMAN, "女性"),
        (GENDER_UNKNOWN, "不明"),
    )
    PROGRESS_APPLY = "apply"
    PROGRESS_CASUAL_INTERVIEW = "casual_interview"
    PROGRESS_FIRST_INTERVIEW = "first_interview"
    PROGRESS_SECOND_INTERVIEW = "second_interview"
    PROGRESS_THIRD_INTERVIEW = "third_interview"
    PROGRESS_FINAL_INTERVIEW = "final_interview"
    PROGRESS_UNOFFICIAL_OFFER = "unofficial_offer"
    PROGRESS_JOINING_THE_COMPANY = "joining_the_company"
    PROGRESS_FOLLOW = "follow"
    PROGRESS = (
        (PROGRESS_APPLY, "応募"),
        (PROGRESS_CASUAL_INTERVIEW, "カジュアル面談"),
        (PROGRESS_FIRST_INTERVIEW, "一次面接"),
        (PROGRESS_SECOND_INTERVIEW, "二次面接"),
        (PROGRESS_THIRD_INTERVIEW, "三次面接"),
        (PROGRESS_FINAL_INTERVIEW, "最終面接"),
        (PROGRESS_UNOFFICIAL_OFFER, "内定"),
        (PROGRESS_JOINING_THE_COMPANY, "入社"),
        (PROGRESS_FOLLOW, "フォロー"),
    )
