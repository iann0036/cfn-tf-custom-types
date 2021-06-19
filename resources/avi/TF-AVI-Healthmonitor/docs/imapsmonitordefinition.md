# TF::AVI::Healthmonitor ImapsMonitorDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#folder" title="Folder">Folder</a>" : <i>String</i>,
    "<a href="#sslattributes" title="SslAttributes">SslAttributes</a>" : <i>[ <a href="sslattributesdefinition.md">SslAttributesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#folder" title="Folder">Folder</a>: <i>String</i>
<a href="#sslattributes" title="SslAttributes">SslAttributes</a>: <i>
      - <a href="sslattributesdefinition.md">SslAttributesDefinition</a></i>
</pre>

## Properties

#### Folder

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SslAttributes

_Required_: No

_Type_: List of <a href="sslattributesdefinition.md">SslAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

