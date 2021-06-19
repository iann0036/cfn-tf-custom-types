# TF::Rancher2::ClusterLogging FluentdConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
    "<a href="#compress" title="Compress">Compress</a>" : <i>Boolean</i>,
    "<a href="#enabletls" title="EnableTls">EnableTls</a>" : <i>Boolean</i>,
    "<a href="#fluentservers" title="FluentServers">FluentServers</a>" : <i>[ <a href="fluentserversdefinition.md">FluentServersDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
<a href="#compress" title="Compress">Compress</a>: <i>Boolean</i>
<a href="#enabletls" title="EnableTls">EnableTls</a>: <i>Boolean</i>
<a href="#fluentservers" title="FluentServers">FluentServers</a>: <i>
      - <a href="fluentserversdefinition.md">FluentServersDefinition</a></i>
</pre>

## Properties

#### Certificate

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Compress

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableTls

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FluentServers

_Required_: No

_Type_: List of <a href="fluentserversdefinition.md">FluentServersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

