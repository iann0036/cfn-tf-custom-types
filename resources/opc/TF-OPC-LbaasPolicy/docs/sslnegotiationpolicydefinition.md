# TF::OPC::LbaasPolicy SslNegotiationPolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#serverorderpreference" title="ServerOrderPreference">ServerOrderPreference</a>" : <i>String</i>,
    "<a href="#sslciphers" title="SslCiphers">SslCiphers</a>" : <i>[ String, ... ]</i>,
    "<a href="#sslprotocol" title="SslProtocol">SslProtocol</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#serverorderpreference" title="ServerOrderPreference">ServerOrderPreference</a>: <i>String</i>
<a href="#sslciphers" title="SslCiphers">SslCiphers</a>: <i>
      - String</i>
<a href="#sslprotocol" title="SslProtocol">SslProtocol</a>: <i>
      - String</i>
</pre>

## Properties

#### Port

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerOrderPreference

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslCiphers

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslProtocol

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

