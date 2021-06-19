# TF::OctopusDeploy::Lifecycle PhaseDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#automaticdeploymenttargets" title="AutomaticDeploymentTargets">AutomaticDeploymentTargets</a>" : <i>[ String, ... ]</i>,
    "<a href="#id" title="Id">Id</a>" : <i>String</i>,
    "<a href="#isoptionalphase" title="IsOptionalPhase">IsOptionalPhase</a>" : <i>Boolean</i>,
    "<a href="#minimumenvironmentsbeforepromotion" title="MinimumEnvironmentsBeforePromotion">MinimumEnvironmentsBeforePromotion</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#optionaldeploymenttargets" title="OptionalDeploymentTargets">OptionalDeploymentTargets</a>" : <i>[ String, ... ]</i>,
    "<a href="#releaseretentionpolicy" title="ReleaseRetentionPolicy">ReleaseRetentionPolicy</a>" : <i>[ <a href="releaseretentionpolicydefinition.md">ReleaseRetentionPolicyDefinition</a>, ... ]</i>,
    "<a href="#tentacleretentionpolicy" title="TentacleRetentionPolicy">TentacleRetentionPolicy</a>" : <i>[ <a href="tentacleretentionpolicydefinition.md">TentacleRetentionPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#automaticdeploymenttargets" title="AutomaticDeploymentTargets">AutomaticDeploymentTargets</a>: <i>
      - String</i>
<a href="#id" title="Id">Id</a>: <i>String</i>
<a href="#isoptionalphase" title="IsOptionalPhase">IsOptionalPhase</a>: <i>Boolean</i>
<a href="#minimumenvironmentsbeforepromotion" title="MinimumEnvironmentsBeforePromotion">MinimumEnvironmentsBeforePromotion</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#optionaldeploymenttargets" title="OptionalDeploymentTargets">OptionalDeploymentTargets</a>: <i>
      - String</i>
<a href="#releaseretentionpolicy" title="ReleaseRetentionPolicy">ReleaseRetentionPolicy</a>: <i>
      - <a href="releaseretentionpolicydefinition.md">ReleaseRetentionPolicyDefinition</a></i>
<a href="#tentacleretentionpolicy" title="TentacleRetentionPolicy">TentacleRetentionPolicy</a>: <i>
      - <a href="tentacleretentionpolicydefinition.md">TentacleRetentionPolicyDefinition</a></i>
</pre>

## Properties

#### AutomaticDeploymentTargets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOptionalPhase

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinimumEnvironmentsBeforePromotion

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OptionalDeploymentTargets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReleaseRetentionPolicy

_Required_: No

_Type_: List of <a href="releaseretentionpolicydefinition.md">ReleaseRetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TentacleRetentionPolicy

_Required_: No

_Type_: List of <a href="tentacleretentionpolicydefinition.md">TentacleRetentionPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

