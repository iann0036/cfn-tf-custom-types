# TF::Rancher2::Cluster EksConfigV2Definition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudcredentialid" title="CloudCredentialId">CloudCredentialId</a>" : <i>String</i>,
    "<a href="#imported" title="Imported">Imported</a>" : <i>Boolean</i>,
    "<a href="#kmskey" title="KmsKey">KmsKey</a>" : <i>String</i>,
    "<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>" : <i>String</i>,
    "<a href="#loggingtypes" title="LoggingTypes">LoggingTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>" : <i>Boolean</i>,
    "<a href="#publicaccess" title="PublicAccess">PublicAccess</a>" : <i>Boolean</i>,
    "<a href="#publicaccesssources" title="PublicAccessSources">PublicAccessSources</a>" : <i>[ String, ... ]</i>,
    "<a href="#region" title="Region">Region</a>" : <i>String</i>,
    "<a href="#secretsencryption" title="SecretsEncryption">SecretsEncryption</a>" : <i>Boolean</i>,
    "<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>" : <i>[ String, ... ]</i>,
    "<a href="#servicerole" title="ServiceRole">ServiceRole</a>" : <i>String</i>,
    "<a href="#subnets" title="Subnets">Subnets</a>" : <i>[ String, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>,
    "<a href="#nodegroups" title="NodeGroups">NodeGroups</a>" : <i>[ <a href="nodegroupsdefinition.md">NodeGroupsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudcredentialid" title="CloudCredentialId">CloudCredentialId</a>: <i>String</i>
<a href="#imported" title="Imported">Imported</a>: <i>Boolean</i>
<a href="#kmskey" title="KmsKey">KmsKey</a>: <i>String</i>
<a href="#kubernetesversion" title="KubernetesVersion">KubernetesVersion</a>: <i>String</i>
<a href="#loggingtypes" title="LoggingTypes">LoggingTypes</a>: <i>
      - String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#privateaccess" title="PrivateAccess">PrivateAccess</a>: <i>Boolean</i>
<a href="#publicaccess" title="PublicAccess">PublicAccess</a>: <i>Boolean</i>
<a href="#publicaccesssources" title="PublicAccessSources">PublicAccessSources</a>: <i>
      - String</i>
<a href="#region" title="Region">Region</a>: <i>String</i>
<a href="#secretsencryption" title="SecretsEncryption">SecretsEncryption</a>: <i>Boolean</i>
<a href="#securitygroups" title="SecurityGroups">SecurityGroups</a>: <i>
      - String</i>
<a href="#servicerole" title="ServiceRole">ServiceRole</a>: <i>String</i>
<a href="#subnets" title="Subnets">Subnets</a>: <i>
      - String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
<a href="#nodegroups" title="NodeGroups">NodeGroups</a>: <i>
      - <a href="nodegroupsdefinition.md">NodeGroupsDefinition</a></i>
</pre>

## Properties

#### CloudCredentialId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Imported

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KubernetesVersion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoggingTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAccessSources

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretsEncryption

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subnets

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NodeGroups

_Required_: No

_Type_: List of <a href="nodegroupsdefinition.md">NodeGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

