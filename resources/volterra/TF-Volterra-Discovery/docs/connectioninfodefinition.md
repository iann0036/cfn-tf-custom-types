# TF::Volterra::Discovery ConnectionInfoDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#apiserver" title="ApiServer">ApiServer</a>" : <i>String</i>,
    "<a href="#tlsinfo" title="TlsInfo">TlsInfo</a>" : <i>[ <a href="tlsinfodefinition.md">TlsInfoDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#apiserver" title="ApiServer">ApiServer</a>: <i>String</i>
<a href="#tlsinfo" title="TlsInfo">TlsInfo</a>: <i>
      - <a href="tlsinfodefinition.md">TlsInfoDefinition</a></i>
</pre>

## Properties

#### ApiServer

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsInfo

_Required_: No

_Type_: List of <a href="tlsinfodefinition.md">TlsInfoDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

