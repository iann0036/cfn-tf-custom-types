# TF::RKE::Cluster KubeApiDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alwayspullimages" title="AlwaysPullImages">AlwaysPullImages</a>" : <i>Boolean</i>,
    "<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>" : <i>[ <a href="extraargsdefinition.md">ExtraArgsDefinition</a>, ... ]</i>,
    "<a href="#extrabinds" title="ExtraBinds">ExtraBinds</a>" : <i>[ String, ... ]</i>,
    "<a href="#extraenv" title="ExtraEnv">ExtraEnv</a>" : <i>[ String, ... ]</i>,
    "<a href="#image" title="Image">Image</a>" : <i>String</i>,
    "<a href="#podsecuritypolicy" title="PodSecurityPolicy">PodSecurityPolicy</a>" : <i>Boolean</i>,
    "<a href="#serviceclusteriprange" title="ServiceClusterIpRange">ServiceClusterIpRange</a>" : <i>String</i>,
    "<a href="#servicenodeportrange" title="ServiceNodePortRange">ServiceNodePortRange</a>" : <i>String</i>,
    "<a href="#auditlog" title="AuditLog">AuditLog</a>" : <i>[ <a href="auditlogdefinition.md">AuditLogDefinition</a>, ... ]</i>,
    "<a href="#eventratelimit" title="EventRateLimit">EventRateLimit</a>" : <i>[ <a href="eventratelimitdefinition.md">EventRateLimitDefinition</a>, ... ]</i>,
    "<a href="#secretsencryptionconfig" title="SecretsEncryptionConfig">SecretsEncryptionConfig</a>" : <i>[ <a href="secretsencryptionconfigdefinition.md">SecretsEncryptionConfigDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#alwayspullimages" title="AlwaysPullImages">AlwaysPullImages</a>: <i>Boolean</i>
<a href="#extraargs" title="ExtraArgs">ExtraArgs</a>: <i>
      - <a href="extraargsdefinition.md">ExtraArgsDefinition</a></i>
<a href="#extrabinds" title="ExtraBinds">ExtraBinds</a>: <i>
      - String</i>
<a href="#extraenv" title="ExtraEnv">ExtraEnv</a>: <i>
      - String</i>
<a href="#image" title="Image">Image</a>: <i>String</i>
<a href="#podsecuritypolicy" title="PodSecurityPolicy">PodSecurityPolicy</a>: <i>Boolean</i>
<a href="#serviceclusteriprange" title="ServiceClusterIpRange">ServiceClusterIpRange</a>: <i>String</i>
<a href="#servicenodeportrange" title="ServiceNodePortRange">ServiceNodePortRange</a>: <i>String</i>
<a href="#auditlog" title="AuditLog">AuditLog</a>: <i>
      - <a href="auditlogdefinition.md">AuditLogDefinition</a></i>
<a href="#eventratelimit" title="EventRateLimit">EventRateLimit</a>: <i>
      - <a href="eventratelimitdefinition.md">EventRateLimitDefinition</a></i>
<a href="#secretsencryptionconfig" title="SecretsEncryptionConfig">SecretsEncryptionConfig</a>: <i>
      - <a href="secretsencryptionconfigdefinition.md">SecretsEncryptionConfigDefinition</a></i>
</pre>

## Properties

#### AlwaysPullImages

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraArgs

_Required_: No

_Type_: List of <a href="extraargsdefinition.md">ExtraArgsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraBinds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExtraEnv

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Image

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PodSecurityPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceClusterIpRange

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceNodePortRange

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuditLog

_Required_: No

_Type_: List of <a href="auditlogdefinition.md">AuditLogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventRateLimit

_Required_: No

_Type_: List of <a href="eventratelimitdefinition.md">EventRateLimitDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretsEncryptionConfig

_Required_: No

_Type_: List of <a href="secretsencryptionconfigdefinition.md">SecretsEncryptionConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

