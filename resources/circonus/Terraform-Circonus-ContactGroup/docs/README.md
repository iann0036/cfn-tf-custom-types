# Terraform::Circonus::ContactGroup

CloudFormation equivalent of circonus_contact_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Circonus::ContactGroup",
    "Properties" : {
        "<a href="#aggregationwindow" title="AggregationWindow">AggregationWindow</a>" : <i>String</i>,
        "<a href="#alwayssendclear" title="AlwaysSendClear">AlwaysSendClear</a>" : <i>Boolean</i>,
        "<a href="#grouptype" title="GroupType">GroupType</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#longmessage" title="LongMessage">LongMessage</a>" : <i>String</i>,
        "<a href="#longsubject" title="LongSubject">LongSubject</a>" : <i>String</i>,
        "<a href="#longsummary" title="LongSummary">LongSummary</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#shortmessage" title="ShortMessage">ShortMessage</a>" : <i>String</i>,
        "<a href="#shortsummary" title="ShortSummary">ShortSummary</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
        "<a href="#alertoption" title="AlertOption">AlertOption</a>" : <i>[ <a href="alertoption.md">AlertOption</a>, ... ]</i>,
        "<a href="#email" title="Email">Email</a>" : <i>[ <a href="email.md">Email</a>, ... ]</i>,
        "<a href="#http" title="Http">Http</a>" : <i>[ <a href="http.md">Http</a>, ... ]</i>,
        "<a href="#irc" title="Irc">Irc</a>" : <i>[ <a href="irc.md">Irc</a>, ... ]</i>,
        "<a href="#pagerduty" title="PagerDuty">PagerDuty</a>" : <i>[ <a href="pagerduty.md">PagerDuty</a>, ... ]</i>,
        "<a href="#slack" title="Slack">Slack</a>" : <i>[ <a href="slack.md">Slack</a>, ... ]</i>,
        "<a href="#sms" title="Sms">Sms</a>" : <i>[ <a href="sms.md">Sms</a>, ... ]</i>,
        "<a href="#victorops" title="Victorops">Victorops</a>" : <i>[ <a href="victorops.md">Victorops</a>, ... ]</i>,
        "<a href="#xmpp" title="Xmpp">Xmpp</a>" : <i>[ <a href="xmpp.md">Xmpp</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Circonus::ContactGroup
Properties:
    <a href="#aggregationwindow" title="AggregationWindow">AggregationWindow</a>: <i>String</i>
    <a href="#alwayssendclear" title="AlwaysSendClear">AlwaysSendClear</a>: <i>Boolean</i>
    <a href="#grouptype" title="GroupType">GroupType</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#longmessage" title="LongMessage">LongMessage</a>: <i>String</i>
    <a href="#longsubject" title="LongSubject">LongSubject</a>: <i>String</i>
    <a href="#longsummary" title="LongSummary">LongSummary</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#shortmessage" title="ShortMessage">ShortMessage</a>: <i>String</i>
    <a href="#shortsummary" title="ShortSummary">ShortSummary</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
    <a href="#alertoption" title="AlertOption">AlertOption</a>: <i>
      - <a href="alertoption.md">AlertOption</a></i>
    <a href="#email" title="Email">Email</a>: <i>
      - <a href="email.md">Email</a></i>
    <a href="#http" title="Http">Http</a>: <i>
      - <a href="http.md">Http</a></i>
    <a href="#irc" title="Irc">Irc</a>: <i>
      - <a href="irc.md">Irc</a></i>
    <a href="#pagerduty" title="PagerDuty">PagerDuty</a>: <i>
      - <a href="pagerduty.md">PagerDuty</a></i>
    <a href="#slack" title="Slack">Slack</a>: <i>
      - <a href="slack.md">Slack</a></i>
    <a href="#sms" title="Sms">Sms</a>: <i>
      - <a href="sms.md">Sms</a></i>
    <a href="#victorops" title="Victorops">Victorops</a>: <i>
      - <a href="victorops.md">Victorops</a></i>
    <a href="#xmpp" title="Xmpp">Xmpp</a>: <i>
      - <a href="xmpp.md">Xmpp</a></i>
</pre>

## Properties

#### AggregationWindow

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlwaysSendClear

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongSubject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LongSummary

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ShortSummary

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlertOption

_Required_: No

_Type_: List of <a href="alertoption.md">AlertOption</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

_Required_: No

_Type_: List of <a href="email.md">Email</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No

_Type_: List of <a href="http.md">Http</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Irc

_Required_: No

_Type_: List of <a href="irc.md">Irc</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PagerDuty

_Required_: No

_Type_: List of <a href="pagerduty.md">PagerDuty</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Slack

_Required_: No

_Type_: List of <a href="slack.md">Slack</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Sms

_Required_: No

_Type_: List of <a href="sms.md">Sms</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Victorops

_Required_: No

_Type_: List of <a href="victorops.md">Victorops</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Xmpp

_Required_: No

_Type_: List of <a href="xmpp.md">Xmpp</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### LastModified

Returns the <code>LastModified</code> value.

#### LastModifiedBy

Returns the <code>LastModifiedBy</code> value.

