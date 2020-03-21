# Terraform::RunScope::Environment Emails

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#notifyall" title="NotifyAll">NotifyAll</a>" : <i>Boolean</i>,
    "<a href="#notifyon" title="NotifyOn">NotifyOn</a>" : <i>String</i>,
    "<a href="#notifythreshold" title="NotifyThreshold">NotifyThreshold</a>" : <i>Double</i>,
    "<a href="#recipients" title="Recipients">Recipients</a>" : <i>[ &lt;a href=&#34;emails-recipients.md&#34;&gt;Recipients&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#notifyall" title="NotifyAll">NotifyAll</a>: <i>Boolean</i>
<a href="#notifyon" title="NotifyOn">NotifyOn</a>: <i>String</i>
<a href="#notifythreshold" title="NotifyThreshold">NotifyThreshold</a>: <i>Double</i>
<a href="#recipients" title="Recipients">Recipients</a>: <i>
      - &lt;a href=&#34;emails-recipients.md&#34;&gt;Recipients&lt;/a&gt;</i>
</pre>

## Properties

#### NotifyAll

_Required_: Yes
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyOn

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NotifyThreshold

_Required_: Yes
_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Recipients

_Required_: No
_Type_: List of &lt;a href=&#34;emails-recipients.md&#34;&gt;Recipients&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

