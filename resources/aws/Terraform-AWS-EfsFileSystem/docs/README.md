# Terraform::AWS::EfsFileSystem

CloudFormation equivalent of aws_efs_file_system

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::EfsFileSystem",
    "Properties" : {
        "<a href="#creationtoken" title="CreationToken">CreationToken</a>" : <i>String</i>,
        "<a href="#encrypted" title="Encrypted">Encrypted</a>" : <i>Boolean</i>,
        "<a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>" : <i>String</i>,
        "<a href="#performancemode" title="PerformanceMode">PerformanceMode</a>" : <i>String</i>,
        "<a href="#provisionedthroughputinmibps" title="ProvisionedThroughputInMibps">ProvisionedThroughputInMibps</a>" : <i>Double</i>,
        "<a href="#referencename" title="ReferenceName">ReferenceName</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#throughputmode" title="ThroughputMode">ThroughputMode</a>" : <i>String</i>,
        "<a href="#lifecyclepolicy" title="LifecyclePolicy">LifecyclePolicy</a>" : <i>[ <a href="lifecyclepolicy.md">LifecyclePolicy</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::EfsFileSystem
Properties:
    <a href="#creationtoken" title="CreationToken">CreationToken</a>: <i>String</i>
    <a href="#encrypted" title="Encrypted">Encrypted</a>: <i>Boolean</i>
    <a href="#kmskeyid" title="KmsKeyId">KmsKeyId</a>: <i>String</i>
    <a href="#performancemode" title="PerformanceMode">PerformanceMode</a>: <i>String</i>
    <a href="#provisionedthroughputinmibps" title="ProvisionedThroughputInMibps">ProvisionedThroughputInMibps</a>: <i>Double</i>
    <a href="#referencename" title="ReferenceName">ReferenceName</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#throughputmode" title="ThroughputMode">ThroughputMode</a>: <i>String</i>
    <a href="#lifecyclepolicy" title="LifecyclePolicy">LifecyclePolicy</a>: <i>
      - <a href="lifecyclepolicy.md">LifecyclePolicy</a></i>
</pre>

## Properties

#### CreationToken

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encrypted

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KmsKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PerformanceMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProvisionedThroughputInMibps

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReferenceName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ThroughputMode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecyclePolicy

_Required_: No

_Type_: List of <a href="lifecyclepolicy.md">LifecyclePolicy</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### DnsName

Returns the <code>DnsName</code> value.

#### Id

Returns the <code>Id</code> value.

