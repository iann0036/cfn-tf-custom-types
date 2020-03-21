# Terraform::Consul::Service Check

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#checkid" title="CheckId">CheckId</a>" : <i>String</i>,
    "<a href="#deregistercriticalserviceafter" title="DeregisterCriticalServiceAfter">DeregisterCriticalServiceAfter</a>" : <i>String</i>,
    "<a href="#http" title="Http">Http</a>" : <i>String</i>,
    "<a href="#interval" title="Interval">Interval</a>" : <i>String</i>,
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#notes" title="Notes">Notes</a>" : <i>String</i>,
    "<a href="#status" title="Status">Status</a>" : <i>String</i>,
    "<a href="#tcp" title="Tcp">Tcp</a>" : <i>String</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>String</i>,
    "<a href="#tlsskipverify" title="TlsSkipVerify">TlsSkipVerify</a>" : <i>Boolean</i>,
    "<a href="#header" title="Header">Header</a>" : <i>[ &lt;a href=&#34;check-header.md&#34;&gt;Header&lt;/a&gt;, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#checkid" title="CheckId">CheckId</a>: <i>String</i>
<a href="#deregistercriticalserviceafter" title="DeregisterCriticalServiceAfter">DeregisterCriticalServiceAfter</a>: <i>String</i>
<a href="#http" title="Http">Http</a>: <i>String</i>
<a href="#interval" title="Interval">Interval</a>: <i>String</i>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#notes" title="Notes">Notes</a>: <i>String</i>
<a href="#status" title="Status">Status</a>: <i>String</i>
<a href="#tcp" title="Tcp">Tcp</a>: <i>String</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>String</i>
<a href="#tlsskipverify" title="TlsSkipVerify">TlsSkipVerify</a>: <i>Boolean</i>
<a href="#header" title="Header">Header</a>: <i>
      - &lt;a href=&#34;check-header.md&#34;&gt;Header&lt;/a&gt;</i>
</pre>

## Properties

#### CheckId

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeregisterCriticalServiceAfter

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Http

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Interval

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Notes

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tcp

_Required_: No
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

_Required_: Yes
_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsSkipVerify

_Required_: No
_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Header

_Required_: No
_Type_: List of &lt;a href=&#34;check-header.md&#34;&gt;Header&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

