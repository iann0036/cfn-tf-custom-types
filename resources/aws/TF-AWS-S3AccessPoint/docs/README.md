# TF::AWS::S3AccessPoint

Provides a resource to manage an S3 Access Point.

-> Advanced usage: To use a custom API endpoint for this Terraform resource, use the [`s3control` endpoint provider configuration](/docs/providers/aws/index.html#s3control), not the `s3` endpoint provider configuration.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::S3AccessPoint",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#policy" title="Policy">Policy</a>" : <i>String</i>,
        "<a href="#publicaccessblockconfiguration" title="PublicAccessBlockConfiguration">PublicAccessBlockConfiguration</a>" : <i>[ <a href="publicaccessblockconfigurationdefinition.md">PublicAccessBlockConfigurationDefinition</a>, ... ]</i>,
        "<a href="#vpcconfiguration" title="VpcConfiguration">VpcConfiguration</a>" : <i>[ <a href="vpcconfigurationdefinition.md">VpcConfigurationDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::S3AccessPoint
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#policy" title="Policy">Policy</a>: <i>String</i>
    <a href="#publicaccessblockconfiguration" title="PublicAccessBlockConfiguration">PublicAccessBlockConfiguration</a>: <i>
      - <a href="publicaccessblockconfigurationdefinition.md">PublicAccessBlockConfigurationDefinition</a></i>
    <a href="#vpcconfiguration" title="VpcConfiguration">VpcConfiguration</a>: <i>
      - <a href="vpcconfigurationdefinition.md">VpcConfigurationDefinition</a></i>
</pre>

## Properties

#### AccountId

The AWS account ID for the owner of the bucket for which you want to create an access point. Defaults to automatically determined account ID of the Terraform AWS provider.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

The name of an AWS Partition S3 Bucket or the Amazon Resource Name (ARN) of S3 on Outposts Bucket that you want to associate this access point with.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name you want to assign to this access point.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policy

A valid JSON document that specifies the policy that you want to apply to this access point.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAccessBlockConfiguration

_Required_: No

_Type_: List of <a href="publicaccessblockconfigurationdefinition.md">PublicAccessBlockConfigurationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcConfiguration

_Required_: No

_Type_: List of <a href="vpcconfigurationdefinition.md">VpcConfigurationDefinition</a>

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

#### DomainName

Returns the <code>DomainName</code> value.

#### HasPublicAccessPolicy

Returns the <code>HasPublicAccessPolicy</code> value.

#### Id

Returns the <code>Id</code> value.

#### NetworkOrigin

Returns the <code>NetworkOrigin</code> value.

