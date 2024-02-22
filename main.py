import data_processing
import chart_display


def main():
    # 获取数据
    try:
        data_processing.get_klines_data()
    except Exception as e:
        print(f"Error in data retrieval: {e}")
        return

    # 处理数据
    # try:
    #     processed_data = data_processing.process_data()
    # except Exception as e:
    #     print(f"Error in data processing: {e}")
    #     return

    # # 显示图表
    # try:
    #     chart_display.display_chart(processed_data)
    # except Exception as e:
    #     print(f"Error in chart display: {e}")
    #     return


if __name__ == "__main__":
    main()
