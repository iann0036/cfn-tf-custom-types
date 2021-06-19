# TF::AVI::Cloud GcpConfigurationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudcredentialsref" title="CloudCredentialsRef">CloudCredentialsRef</a>" : <i>String</i>,
    "<a href="#firewalltargettags" title="FirewallTargetTags">FirewallTargetTags</a>" : <i>[ String, ... ]</i>,
    "<a href="#gcsbucketname" title="GcsBucketName">GcsBucketName</a>" : <i>String</i>,
    "<a href="#gcsprojectid" title="GcsProjectId">GcsProjectId</a>" : <i>String</i>,
    "<a href="#regionname" title="RegionName">RegionName</a>" : <i>String</i>,
    "<a href="#seprojectid" title="SeProjectId">SeProjectId</a>" : <i>String</i>,
    "<a href="#zones" title="Zones">Zones</a>" : <i>[ <a href="zonesdefinition.md">ZonesDefinition</a>, ... ]</i>,
    "<a href="#encryptionkeys" title="EncryptionKeys">EncryptionKeys</a>" : <i>[ <a href="encryptionkeysdefinition.md">EncryptionKeysDefinition</a>, ... ]</i>,
    "<a href="#networkconfig" title="NetworkConfig">NetworkConfig</a>" : <i>[ <a href="networkconfigdefinition.md">NetworkConfigDefinition</a>, ... ]</i>,
    "<a href="#vipallocationstrategy" title="VipAllocationStrategy">VipAllocationStrategy</a>" : <i>[ <a href="vipallocationstrategydefinition.md">VipAllocationStrategyDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudcredentialsref" title="CloudCredentialsRef">CloudCredentialsRef</a>: <i>String</i>
<a href="#firewalltargettags" title="FirewallTargetTags">FirewallTargetTags</a>: <i>
      - String</i>
<a href="#gcsbucketname" title="GcsBucketName">GcsBucketName</a>: <i>String</i>
<a href="#gcsprojectid" title="GcsProjectId">GcsProjectId</a>: <i>String</i>
<a href="#regionname" title="RegionName">RegionName</a>: <i>String</i>
<a href="#seprojectid" title="SeProjectId">SeProjectId</a>: <i>String</i>
<a href="#zones" title="Zones">Zones</a>: <i>
      - <a href="zonesdefinition.md">ZonesDefinition</a></i>
<a href="#encryptionkeys" title="EncryptionKeys">EncryptionKeys</a>: <i>
      - <a href="encryptionkeysdefinition.md">EncryptionKeysDefinition</a></i>
<a href="#networkconfig" title="NetworkConfig">NetworkConfig</a>: <i>
      - <a href="networkconfigdefinition.md">NetworkConfigDefinition</a></i>
<a href="#vipallocationstrategy" title="VipAllocationStrategy">VipAllocationStrategy</a>: <i>
      - <a href="vipallocationstrategydefinition.md">VipAllocationStrategyDefinition</a></i>
</pre>

## Properties

#### CloudCredentialsRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirewallTargetTags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsBucketName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GcsProjectId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegionName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SeProjectId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Zones

_Required_: Yes

_Type_: List of <a href="zonesdefinition.md">ZonesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionKeys

_Required_: No

_Type_: List of <a href="encryptionkeysdefinition.md">EncryptionKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NetworkConfig

_Required_: No

_Type_: List of <a href="networkconfigdefinition.md">NetworkConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VipAllocationStrategy

_Required_: No

_Type_: List of <a href="vipallocationstrategydefinition.md">VipAllocationStrategyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

