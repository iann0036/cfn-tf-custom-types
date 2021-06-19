# TF::Databricks::MwsVpcEndpoint

CloudFormation equivalent of databricks_mws_vpc_endpoint

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::MwsVpcEndpoint",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>" : <i>String</i>,
        "<a href="#awsendpointserviceid" title="AwsEndpointServiceId">AwsEndpointServiceId</a>" : <i>String</i>,
        "<a href="#awsvpcendpointid" title="AwsVpcEndpointId">AwsVpcEndpointId</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#usecase" title="UseCase">UseCase</a>" : <i>String</i>,
        "<a href="#vpcendpointid" title="VpcEndpointId">VpcEndpointId</a>" : <i>String</i>,
        "<a href="#vpcendpointname" title="VpcEndpointName">VpcEndpointName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::MwsVpcEndpoint
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#awsaccountid" title="AwsAccountId">AwsAccountId</a>: <i>String</i>
    <a href="#awsendpointserviceid" title="AwsEndpointServiceId">AwsEndpointServiceId</a>: <i>String</i>
    <a href="#awsvpcendpointid" title="AwsVpcEndpointId">AwsVpcEndpointId</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#usecase" title="UseCase">UseCase</a>: <i>String</i>
    <a href="#vpcendpointid" title="VpcEndpointId">VpcEndpointId</a>: <i>String</i>
    <a href="#vpcendpointname" title="VpcEndpointName">VpcEndpointName</a>: <i>String</i>
</pre>

## Properties

#### AccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsAccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsEndpointServiceId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsVpcEndpointId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCase

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcEndpointId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VpcEndpointName

_Required_: Yes

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

#### Id

Returns the <code>Id</code> value.

