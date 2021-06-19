# TF::Alicloud::CmsAlarmContact

CloudFormation equivalent of alicloud_cms_alarm_contact

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CmsAlarmContact",
    "Properties" : {
        "<a href="#alarmcontactname" title="AlarmContactName">AlarmContactName</a>" : <i>String</i>,
        "<a href="#channelsaliim" title="ChannelsAliim">ChannelsAliim</a>" : <i>String</i>,
        "<a href="#channelsdingwebhook" title="ChannelsDingWebHook">ChannelsDingWebHook</a>" : <i>String</i>,
        "<a href="#channelsmail" title="ChannelsMail">ChannelsMail</a>" : <i>String</i>,
        "<a href="#channelssms" title="ChannelsSms">ChannelsSms</a>" : <i>String</i>,
        "<a href="#describe" title="Describe">Describe</a>" : <i>String</i>,
        "<a href="#lang" title="Lang">Lang</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CmsAlarmContact
Properties:
    <a href="#alarmcontactname" title="AlarmContactName">AlarmContactName</a>: <i>String</i>
    <a href="#channelsaliim" title="ChannelsAliim">ChannelsAliim</a>: <i>String</i>
    <a href="#channelsdingwebhook" title="ChannelsDingWebHook">ChannelsDingWebHook</a>: <i>String</i>
    <a href="#channelsmail" title="ChannelsMail">ChannelsMail</a>: <i>String</i>
    <a href="#channelssms" title="ChannelsSms">ChannelsSms</a>: <i>String</i>
    <a href="#describe" title="Describe">Describe</a>: <i>String</i>
    <a href="#lang" title="Lang">Lang</a>: <i>String</i>
</pre>

## Properties

#### AlarmContactName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChannelsAliim

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChannelsDingWebHook

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChannelsMail

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChannelsSms

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Describe

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lang

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

