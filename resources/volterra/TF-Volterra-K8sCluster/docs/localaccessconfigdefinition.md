# TF::Volterra::K8sCluster LocalAccessConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultport" title="DefaultPort">DefaultPort</a>" : <i>Boolean</i>,
    "<a href="#localdomain" title="LocalDomain">LocalDomain</a>" : <i>[ <a href="localdomaindefinition.md">LocalDomainDefinition</a>, ... ]</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#defaultport" title="DefaultPort">DefaultPort</a>: <i>Boolean</i>
<a href="#localdomain" title="LocalDomain">LocalDomain</a>: <i>
      - <a href="localdomaindefinition.md">LocalDomainDefinition</a></i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
</pre>

## Properties

#### DefaultPort

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalDomain

_Required_: No

_Type_: List of <a href="localdomaindefinition.md">LocalDomainDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

