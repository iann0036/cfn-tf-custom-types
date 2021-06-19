# TF::SDM::Resource AwsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
    "<a href="#egressfilter" title="EgressFilter">EgressFilter</a>" : <i>String</i>,
    "<a href="#healthcheckregion" title="HealthcheckRegion">HealthcheckRegion</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
    "<a href="#roleexternalid" title="RoleExternalId">RoleExternalId</a>" : <i>String</i>,
    "<a href="#secretaccesskey" title="SecretAccessKey">SecretAccessKey</a>" : <i>String</i>,
    "<a href="#secretstoreaccesskeykey" title="SecretStoreAccessKeyKey">SecretStoreAccessKeyKey</a>" : <i>String</i>,
    "<a href="#secretstoreaccesskeypath" title="SecretStoreAccessKeyPath">SecretStoreAccessKeyPath</a>" : <i>String</i>,
    "<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>" : <i>String</i>,
    "<a href="#secretstorerolearnkey" title="SecretStoreRoleArnKey">SecretStoreRoleArnKey</a>" : <i>String</i>,
    "<a href="#secretstorerolearnpath" title="SecretStoreRoleArnPath">SecretStoreRoleArnPath</a>" : <i>String</i>,
    "<a href="#secretstoreroleexternalidkey" title="SecretStoreRoleExternalIdKey">SecretStoreRoleExternalIdKey</a>" : <i>String</i>,
    "<a href="#secretstoreroleexternalidpath" title="SecretStoreRoleExternalIdPath">SecretStoreRoleExternalIdPath</a>" : <i>String</i>,
    "<a href="#secretstoresecretaccesskeykey" title="SecretStoreSecretAccessKeyKey">SecretStoreSecretAccessKeyKey</a>" : <i>String</i>,
    "<a href="#secretstoresecretaccesskeypath" title="SecretStoreSecretAccessKeyPath">SecretStoreSecretAccessKeyPath</a>" : <i>String</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tagsdefinition.md">TagsDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
<a href="#egressfilter" title="EgressFilter">EgressFilter</a>: <i>String</i>
<a href="#healthcheckregion" title="HealthcheckRegion">HealthcheckRegion</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
<a href="#roleexternalid" title="RoleExternalId">RoleExternalId</a>: <i>String</i>
<a href="#secretaccesskey" title="SecretAccessKey">SecretAccessKey</a>: <i>String</i>
<a href="#secretstoreaccesskeykey" title="SecretStoreAccessKeyKey">SecretStoreAccessKeyKey</a>: <i>String</i>
<a href="#secretstoreaccesskeypath" title="SecretStoreAccessKeyPath">SecretStoreAccessKeyPath</a>: <i>String</i>
<a href="#secretstoreid" title="SecretStoreId">SecretStoreId</a>: <i>String</i>
<a href="#secretstorerolearnkey" title="SecretStoreRoleArnKey">SecretStoreRoleArnKey</a>: <i>String</i>
<a href="#secretstorerolearnpath" title="SecretStoreRoleArnPath">SecretStoreRoleArnPath</a>: <i>String</i>
<a href="#secretstoreroleexternalidkey" title="SecretStoreRoleExternalIdKey">SecretStoreRoleExternalIdKey</a>: <i>String</i>
<a href="#secretstoreroleexternalidpath" title="SecretStoreRoleExternalIdPath">SecretStoreRoleExternalIdPath</a>: <i>String</i>
<a href="#secretstoresecretaccesskeykey" title="SecretStoreSecretAccessKeyKey">SecretStoreSecretAccessKeyKey</a>: <i>String</i>
<a href="#secretstoresecretaccesskeypath" title="SecretStoreSecretAccessKeyPath">SecretStoreSecretAccessKeyPath</a>: <i>String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tagsdefinition.md">TagsDefinition</a></i>
</pre>

## Properties

#### AccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EgressFilter

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthcheckRegion

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleExternalId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretAccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreAccessKeyKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreAccessKeyPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreRoleArnKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreRoleArnPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreRoleExternalIdKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreRoleExternalIdPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreSecretAccessKeyKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretStoreSecretAccessKeyPath

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tagsdefinition.md">TagsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

