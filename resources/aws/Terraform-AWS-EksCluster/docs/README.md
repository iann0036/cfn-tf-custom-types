# Terraform::AWS::EksCluster

Manages an EKS Cluster.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EksCluster",
    "Properties" : {
        "<a href="#enabledclusterlogtypes" title="EnabledClusterLogTypes">EnabledClusterLogTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#rolearn" title="RoleArn">RoleArn</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#version" title="Version">Version</a>" : <i>String</i>,
        "<a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>" : <i>[ <a href="encryptionconfig.md">EncryptionConfig</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeouts.md">Timeouts</a></i>,
        "<a href="#vpcconfig" title="VpcConfig">VpcConfig</a>" : <i>[ <a href="vpcconfig.md">VpcConfig</a>, ... ]</i>,
        "<a href="#provider" title="Provider">Provider</a>" : <i>[ <a href="provider.md">Provider</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EksCluster
Properties:
    <a href="#enabledclusterlogtypes" title="EnabledClusterLogTypes">EnabledClusterLogTypes</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#rolearn" title="RoleArn">RoleArn</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#version" title="Version">Version</a>: <i>String</i>
    <a href="#encryptionconfig" title="EncryptionConfig">EncryptionConfig</a>: <i>
      - <a href="encryptionconfig.md">EncryptionConfig</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeouts.md">Timeouts</a></i>
    <a href="#vpcconfig" title="VpcConfig">VpcConfig</a>: <i>
      - <a href="vpcconfig.md">VpcConfig</a></i>
    <a href="#provider" title="Provider">Provider</a>: <i>
      - <a href="provider.md">Provider</a></i>
</pre>

## Properties

#### EnabledClusterLogTypes

A list of the desired control plane logging to enable. For more information, see [Amazon EKS Control Plane Logging](https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleArn

The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf. Ensure the resource configuration includes explicit dependencies on the IAM Role permissions by adding [`depends_on`](/docs/configuration/resources.html#depends_on-explicit-resource-dependencies) if using the [`aws_iam_role_policy` resource](/docs/providers/aws/r/iam_role_policy.html) or [`aws_iam_role_policy_attachment` resource](/docs/providers/aws/r/iam_role_policy_attachment.html), otherwise EKS cannot delete EKS managed EC2 infrastructure such as Security Groups on EKS Cluster deletion.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

Key-value mapping of resource tags.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Version

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EncryptionConfig

_Required_: No

_Type_: List of <a href="encryptionconfig.md">EncryptionConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeouts.md">Timeouts</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfig

_Required_: No

_Type_: List of <a href="vpcconfig.md">VpcConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Provider

_Required_: No

_Type_: List of <a href="provider.md">Provider</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### CertificateAuthority

Returns the <code>CertificateAuthority</code> value.

#### CreatedAt

Returns the <code>CreatedAt</code> value.

#### Endpoint

Returns the <code>Endpoint</code> value.

#### Id

Returns the <code>Id</code> value.

#### Identity

Returns the <code>Identity</code> value.

#### PlatformVersion

Returns the <code>PlatformVersion</code> value.

#### Status

Returns the <code>Status</code> value.

