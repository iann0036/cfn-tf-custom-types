# TF::Lacework::IntegrationEcr

Use this resource to integrate an Amazon Container Registry (ECR) with Lacework to assess, identify,
and report vulnerabilities found in the operating system software packages in a Docker container
image.

~> **Note:** Assessing a retagged ECR image is not supported because ECR does not consider it a new
image and does not create a new entry. To assess a retagged image, use on-demand assessment through
the Lacework CLI. For more information, see the [container vulnerability section in the Lacework CLI
documentation](https://github.com/lacework/go-sdk/wiki/CLI-Documentation#container-vulnerability-assessments).

This resource has two authentication methods:

* AWS Access Key-Based Authentication
* AWS IAM Role-Based Authentication

!> **Warning:** It is possible to switch authentication methods but the resource
will be destroyed and recreated. This will generate a new `INT_GUID`.

For more information, see [Integrate Amazon Container Registry documentation](https://support.lacework.com/hc/en-us/articles/36...

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Lacework::IntegrationEcr",
    "Properties" : {
        "<a href="#enabled" title="Enabled">Enabled</a>" : <i>Boolean</i>,
        "<a href="#limitbylabel" title="LimitByLabel">LimitByLabel</a>" : <i>String</i>,
        "<a href="#limitbyrepos" title="LimitByRepos">LimitByRepos</a>" : <i>String</i>,
        "<a href="#limitbytag" title="LimitByTag">LimitByTag</a>" : <i>String</i>,
        "<a href="#limitnumimgs" title="LimitNumImgs">LimitNumImgs</a>" : <i>Double</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#registrydomain" title="RegistryDomain">RegistryDomain</a>" : <i>String</i>,
        "<a href="#credentials" title="Credentials">Credentials</a>" : <i>[ <a href="credentialsdefinition.md">CredentialsDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Lacework::IntegrationEcr
Properties:
    <a href="#enabled" title="Enabled">Enabled</a>: <i>Boolean</i>
    <a href="#limitbylabel" title="LimitByLabel">LimitByLabel</a>: <i>String</i>
    <a href="#limitbyrepos" title="LimitByRepos">LimitByRepos</a>: <i>String</i>
    <a href="#limitbytag" title="LimitByTag">LimitByTag</a>: <i>String</i>
    <a href="#limitnumimgs" title="LimitNumImgs">LimitNumImgs</a>: <i>Double</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#registrydomain" title="RegistryDomain">RegistryDomain</a>: <i>String</i>
    <a href="#credentials" title="Credentials">Credentials</a>: <i>
      - <a href="credentialsdefinition.md">CredentialsDefinition</a></i>
</pre>

## Properties

#### Enabled

The state of the external integration. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitByLabel

An image label to limit the assessment of images with matching label. If you specify `limit_by_tag` and `limit_by_label` limits, they function as an `AND`. Supported field input are `mytext*mytext`, `mytext`, `mytext*`, or `mytext`. Only one `*` wildcard is supported. Defaults to `*`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitByRepos

A comma-separated list of repositories to assess. (without spaces recommended).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitByTag

An image tag to limit the assessment of images with matching tag. If you specify `limit_by_tag` and `limit_by_label` limits, they function as an `AND`. Supported field input are `mytext*mytext`, `mytext`, `mytext*`, or `mytext`. Only one `*` wildcard is supported. Defaults to `*`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LimitNumImgs

The maximum number of newest container images to assess per repository. Must be one of `5`, `10`, or `15`. Defaults to `5`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The ECR integration name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryDomain

The Amazon Container Registry (ECR) domain in the format `YourAWSAccount.dkr.ecr.YourRegion.amazonaws.com`, where `YourAWSAcount` is the AWS account number for the AWS IAM user that has a role with permissions to access the ECR and `YourRegion` is your AWS region such as `us-west-2`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Credentials

_Required_: No

_Type_: List of <a href="credentialsdefinition.md">CredentialsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AwsAuthType

Returns the <code>AwsAuthType</code> value.

#### CreatedOrUpdatedBy

Returns the <code>CreatedOrUpdatedBy</code> value.

#### CreatedOrUpdatedTime

Returns the <code>CreatedOrUpdatedTime</code> value.

#### Id

Returns the <code>Id</code> value.

#### IntgGuid

Returns the <code>IntgGuid</code> value.

#### OrgLevel

Returns the <code>OrgLevel</code> value.

#### TypeName

Returns the <code>TypeName</code> value.

