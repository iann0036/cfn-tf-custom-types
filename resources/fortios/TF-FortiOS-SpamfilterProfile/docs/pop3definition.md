# TF::FortiOS::SpamfilterProfile Pop3Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#log" title="Log">Log</a>" : <i>String</i>,
    "<a href="#tagmsg" title="TagMsg">TagMsg</a>" : <i>String</i>,
    "<a href="#tagtype" title="TagType">TagType</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#log" title="Log">Log</a>: <i>String</i>
<a href="#tagmsg" title="TagMsg">TagMsg</a>: <i>String</i>
<a href="#tagtype" title="TagType">TagType</a>: <i>String</i>
</pre>

## Properties

#### Action

Action for spam email. Valid values: `pass`, `tag`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Log

Enable/disable logging. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagMsg

Subject text or header added to spam email.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TagType

Tag subject or header for spam email. Valid values: `subject`, `header`, `spaminfo`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

