# Terraform::AWS::IamServiceLinkedRole

Provides an [IAM service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::IamServiceLinkedRole",
    "Properties" : {
        "<a href="#awsservicename" title="AwsServiceName">AwsServiceName</a>" : <i>String</i>,
        "<a href="#customsuffix" title="CustomSuffix">CustomSuffix</a>" : <i>String</i>,
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::IamServiceLinkedRole
Properties:
    <a href="#awsservicename" title="AwsServiceName">AwsServiceName</a>: <i>String</i>
    <a href="#customsuffix" title="CustomSuffix">CustomSuffix</a>: <i>String</i>
    <a href="#description" title="Description">Description</a>: <i>String</i>
</pre>

## Properties

#### AwsServiceName

The AWS service to which this role is attached. You use a string similar to a URL but without the `http://` in front. For example: `elasticbeanstalk.amazonaws.com`. To find the full list of services that support service-linked roles, check [the docs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSuffix

Additional string appended to the role name. Not all AWS services support custom suffixes.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

The description of the role.

_Required_: No

_Type_: String

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

#### CreateDate

Returns the <code>CreateDate</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### Path

Returns the <code>Path</code> value.

#### UniqueId

Returns the <code>UniqueId</code> value.

