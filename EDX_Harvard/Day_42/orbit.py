def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    spacecraft.update({"distance":0.01, "orbit":"sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    =========== REPORT =======
    
    Name: {spacecraft.get("name", "unkown")}
    Distance: {spacecraft.get("distance", "unkown")} AU
    Orbit: {spacecraft.get("orbit", "unkown")}

    ==========================
    """
main()
