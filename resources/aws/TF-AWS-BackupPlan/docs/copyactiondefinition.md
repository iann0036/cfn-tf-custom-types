# TF::AWS::BackupPlan CopyActionDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#destinationvaultarn" title="DestinationVaultArn">DestinationVaultArn</a>" : <i>String</i>,
    "<a href="#lifecycle" title="Lifecycle">Lifecycle</a>" : <i>[ <a href="lifecycledefinition.md">LifecycleDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#destinationvaultarn" title="DestinationVaultArn">DestinationVaultArn</a>: <i>String</i>
<a href="#lifecycle" title="Lifecycle">Lifecycle</a>: <i>
      - <a href="lifecycledefinition.md">LifecycleDefinition</a></i>
</pre>

## Properties

#### DestinationVaultArn

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Lifecycle

_Required_: No

_Type_: List of <a href="lifecycledefinition.md">LifecycleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

