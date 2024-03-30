// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from custom_interfaces:srv/VideoFrame.idl
// generated code does not contain a copyright notice

#ifndef CUSTOM_INTERFACES__SRV__DETAIL__VIDEO_FRAME__BUILDER_HPP_
#define CUSTOM_INTERFACES__SRV__DETAIL__VIDEO_FRAME__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "custom_interfaces/srv/detail/video_frame__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_VideoFrame_Request_image
{
public:
  Init_VideoFrame_Request_image()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::custom_interfaces::srv::VideoFrame_Request image(::custom_interfaces::srv::VideoFrame_Request::_image_type arg)
  {
    msg_.image = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::VideoFrame_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::VideoFrame_Request>()
{
  return custom_interfaces::srv::builder::Init_VideoFrame_Request_image();
}

}  // namespace custom_interfaces


namespace custom_interfaces
{

namespace srv
{

namespace builder
{

class Init_VideoFrame_Response_ids
{
public:
  explicit Init_VideoFrame_Response_ids(::custom_interfaces::srv::VideoFrame_Response & msg)
  : msg_(msg)
  {}
  ::custom_interfaces::srv::VideoFrame_Response ids(::custom_interfaces::srv::VideoFrame_Response::_ids_type arg)
  {
    msg_.ids = std::move(arg);
    return std::move(msg_);
  }

private:
  ::custom_interfaces::srv::VideoFrame_Response msg_;
};

class Init_VideoFrame_Response_corners
{
public:
  Init_VideoFrame_Response_corners()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_VideoFrame_Response_ids corners(::custom_interfaces::srv::VideoFrame_Response::_corners_type arg)
  {
    msg_.corners = std::move(arg);
    return Init_VideoFrame_Response_ids(msg_);
  }

private:
  ::custom_interfaces::srv::VideoFrame_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::custom_interfaces::srv::VideoFrame_Response>()
{
  return custom_interfaces::srv::builder::Init_VideoFrame_Response_corners();
}

}  // namespace custom_interfaces

#endif  // CUSTOM_INTERFACES__SRV__DETAIL__VIDEO_FRAME__BUILDER_HPP_
