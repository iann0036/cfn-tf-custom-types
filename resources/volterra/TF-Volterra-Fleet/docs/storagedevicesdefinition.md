# TF::Volterra::Fleet StorageDevicesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#advancedadvancedparameters" title="AdvancedAdvancedParameters">AdvancedAdvancedParameters</a>" : <i>[ <a href="advancedadvancedparametersdefinition.md">AdvancedAdvancedParametersDefinition</a>, ... ]</i>,
    "<a href="#storagedevice" title="StorageDevice">StorageDevice</a>" : <i>String</i>,
    "<a href="#netapptrident" title="NetappTrident">NetappTrident</a>" : <i>[ <a href="netapptridentdefinition.md">NetappTridentDefinition</a>, ... ]</i>,
    "<a href="#openebsenterprise" title="OpenebsEnterprise">OpenebsEnterprise</a>" : <i>[ <a href="openebsenterprisedefinition.md">OpenebsEnterpriseDefinition</a>, ... ]</i>,
    "<a href="#pureserviceorchestrator" title="PureServiceOrchestrator">PureServiceOrchestrator</a>" : <i>[ <a href="pureserviceorchestratordefinition.md">PureServiceOrchestratorDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#advancedadvancedparameters" title="AdvancedAdvancedParameters">AdvancedAdvancedParameters</a>: <i>
      - <a href="advancedadvancedparametersdefinition.md">AdvancedAdvancedParametersDefinition</a></i>
<a href="#storagedevice" title="StorageDevice">StorageDevice</a>: <i>String</i>
<a href="#netapptrident" title="NetappTrident">NetappTrident</a>: <i>
      - <a href="netapptridentdefinition.md">NetappTridentDefinition</a></i>
<a href="#openebsenterprise" title="OpenebsEnterprise">OpenebsEnterprise</a>: <i>
      - <a href="openebsenterprisedefinition.md">OpenebsEnterpriseDefinition</a></i>
<a href="#pureserviceorchestrator" title="PureServiceOrchestrator">PureServiceOrchestrator</a>: <i>
      - <a href="pureserviceorchestratordefinition.md">PureServiceOrchestratorDefinition</a></i>
</pre>

## Properties

#### AdvancedAdvancedParameters

_Required_: No

_Type_: List of <a href="advancedadvancedparametersdefinition.md">AdvancedAdvancedParametersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageDevice

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetappTrident

_Required_: No

_Type_: List of <a href="netapptridentdefinition.md">NetappTridentDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OpenebsEnterprise

_Required_: No

_Type_: List of <a href="openebsenterprisedefinition.md">OpenebsEnterpriseDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PureServiceOrchestrator

_Required_: No

_Type_: List of <a href="pureserviceorchestratordefinition.md">PureServiceOrchestratorDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

