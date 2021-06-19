# TF::TencentCloud::MonitorBindingReceiver ReceiversDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endtime" title="EndTime">EndTime</a>" : <i>Double</i>,
    "<a href="#notifyway" title="NotifyWay">NotifyWay</a>" : <i>[ String, ... ]</i>,
    "<a href="#receivelanguage" title="ReceiveLanguage">ReceiveLanguage</a>" : <i>String</i>,
    "<a href="#receivergrouplist" title="ReceiverGroupList">ReceiverGroupList</a>" : <i>[ Double, ... ]</i>,
    "<a href="#receivertype" title="ReceiverType">ReceiverType</a>" : <i>String</i>,
    "<a href="#receiveruserlist" title="ReceiverUserList">ReceiverUserList</a>" : <i>[ Double, ... ]</i>,
    "<a href="#starttime" title="StartTime">StartTime</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#endtime" title="EndTime">EndTime</a>: <i>Double</i>
<a href="#notifyway" title="NotifyWay">NotifyWay</a>: <i>
      - String</i>
<a href="#receivelanguage" title="ReceiveLanguage">ReceiveLanguage</a>: <i>String</i>
<a href="#receivergrouplist" title="ReceiverGroupList">ReceiverGroupList</a>: <i>
      - Double</i>
<a href="#receivertype" title="ReceiverType">ReceiverType</a>: <i>String</i>
<a href="#receiveruserlist" title="ReceiverUserList">ReceiverUserList</a>: <i>
      - Double</i>
<a href="#starttime" title="StartTime">StartTime</a>: <i>Double</i>
</pre>

## Properties

#### EndTime

End of alarm period. Meaning with `start_time`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyWay

Method of warning notification.Optional `CALL`,`EMAIL`,`SITE`,`SMS`,`WECHAT`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiveLanguage

Alert sending language. Optional `en-US`,`zh-CN`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiverGroupList

Alarm receive group ID list.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiverType

Receive type. Optional `group`,`user`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReceiverUserList

Alarm receiver ID list.

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StartTime

Alarm period start time. Valid value ranges: (0~86399). which removes the date after it is converted to Beijing time as a Unix timestamp, for example 7200 means '10:0:0'.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

