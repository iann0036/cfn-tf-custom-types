# TF::AzureRM::ServiceFabricCluster UpgradePolicyDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#forcerestartenabled" title="ForceRestartEnabled">ForceRestartEnabled</a>" : <i>Boolean</i>,
    "<a href="#healthcheckretrytimeout" title="HealthCheckRetryTimeout">HealthCheckRetryTimeout</a>" : <i>String</i>,
    "<a href="#healthcheckstableduration" title="HealthCheckStableDuration">HealthCheckStableDuration</a>" : <i>String</i>,
    "<a href="#healthcheckwaitduration" title="HealthCheckWaitDuration">HealthCheckWaitDuration</a>" : <i>String</i>,
    "<a href="#upgradedomaintimeout" title="UpgradeDomainTimeout">UpgradeDomainTimeout</a>" : <i>String</i>,
    "<a href="#upgradereplicasetchecktimeout" title="UpgradeReplicaSetCheckTimeout">UpgradeReplicaSetCheckTimeout</a>" : <i>String</i>,
    "<a href="#upgradetimeout" title="UpgradeTimeout">UpgradeTimeout</a>" : <i>String</i>,
    "<a href="#deltahealthpolicy" title="DeltaHealthPolicy">DeltaHealthPolicy</a>" : <i>[ <a href="deltahealthpolicydefinition.md">DeltaHealthPolicyDefinition</a>, ... ]</i>,
    "<a href="#healthpolicy" title="HealthPolicy">HealthPolicy</a>" : <i>[ <a href="healthpolicydefinition.md">HealthPolicyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#forcerestartenabled" title="ForceRestartEnabled">ForceRestartEnabled</a>: <i>Boolean</i>
<a href="#healthcheckretrytimeout" title="HealthCheckRetryTimeout">HealthCheckRetryTimeout</a>: <i>String</i>
<a href="#healthcheckstableduration" title="HealthCheckStableDuration">HealthCheckStableDuration</a>: <i>String</i>
<a href="#healthcheckwaitduration" title="HealthCheckWaitDuration">HealthCheckWaitDuration</a>: <i>String</i>
<a href="#upgradedomaintimeout" title="UpgradeDomainTimeout">UpgradeDomainTimeout</a>: <i>String</i>
<a href="#upgradereplicasetchecktimeout" title="UpgradeReplicaSetCheckTimeout">UpgradeReplicaSetCheckTimeout</a>: <i>String</i>
<a href="#upgradetimeout" title="UpgradeTimeout">UpgradeTimeout</a>: <i>String</i>
<a href="#deltahealthpolicy" title="DeltaHealthPolicy">DeltaHealthPolicy</a>: <i>
      - <a href="deltahealthpolicydefinition.md">DeltaHealthPolicyDefinition</a></i>
<a href="#healthpolicy" title="HealthPolicy">HealthPolicy</a>: <i>
      - <a href="healthpolicydefinition.md">HealthPolicyDefinition</a></i>
</pre>

## Properties

#### ForceRestartEnabled

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckRetryTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckStableDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckWaitDuration

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeDomainTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeReplicaSetCheckTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UpgradeTimeout

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DeltaHealthPolicy

_Required_: No

_Type_: List of <a href="deltahealthpolicydefinition.md">DeltaHealthPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthPolicy

_Required_: No

_Type_: List of <a href="healthpolicydefinition.md">HealthPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

