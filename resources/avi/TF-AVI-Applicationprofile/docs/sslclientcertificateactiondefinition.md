# TF::AVI::Applicationprofile SslClientCertificateActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#closeconnection" title="CloseConnection">CloseConnection</a>" : <i>Boolean</i>,
    "<a href="#headers" title="Headers">Headers</a>" : <i>[ <a href="headersdefinition.md">HeadersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#closeconnection" title="CloseConnection">CloseConnection</a>: <i>Boolean</i>
<a href="#headers" title="Headers">Headers</a>: <i>
      - <a href="headersdefinition.md">HeadersDefinition</a></i>
</pre>

## Properties

#### CloseConnection

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Headers

_Required_: No

_Type_: List of <a href="headersdefinition.md">HeadersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

