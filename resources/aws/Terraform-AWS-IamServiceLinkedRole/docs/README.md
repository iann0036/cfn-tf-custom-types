# Terraform::AWS::IamServiceLinkedRole

CloudFormation equivalent of aws_iam_service_linked_role

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
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
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
    <a href="#id" title="Id">Id</a>: <i>String</i>
</pre>

## Properties

#### AwsServiceName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomSuffix

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

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

Returns the &lt;code&gt;Arn&lt;/code&gt; value.

#### CreateDate

Returns the &lt;code&gt;CreateDate&lt;/code&gt; value.

#### Name

Returns the &lt;code&gt;Name&lt;/code&gt; value.

#### Path

Returns the &lt;code&gt;Path&lt;/code&gt; value.

#### UniqueId

Returns the &lt;code&gt;UniqueId&lt;/code&gt; value.

