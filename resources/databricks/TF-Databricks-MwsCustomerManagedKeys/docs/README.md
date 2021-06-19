# TF::Databricks::MwsCustomerManagedKeys

CloudFormation equivalent of databricks_mws_customer_managed_keys

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Databricks::MwsCustomerManagedKeys",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#creationtime" title="CreationTime">CreationTime</a>" : <i>Double</i>,
        "<a href="#customermanagedkeyid" title="CustomerManagedKeyId">CustomerManagedKeyId</a>" : <i>String</i>,
        "<a href="#usecases" title="UseCases">UseCases</a>" : <i>[ String, ... ]</i>,
        "<a href="#awskeyinfo" title="AwsKeyInfo">AwsKeyInfo</a>" : <i>[ <a href="awskeyinfodefinition.md">AwsKeyInfoDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Databricks::MwsCustomerManagedKeys
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#creationtime" title="CreationTime">CreationTime</a>: <i>Double</i>
    <a href="#customermanagedkeyid" title="CustomerManagedKeyId">CustomerManagedKeyId</a>: <i>String</i>
    <a href="#usecases" title="UseCases">UseCases</a>: <i>
      - String</i>
    <a href="#awskeyinfo" title="AwsKeyInfo">AwsKeyInfo</a>: <i>
      - <a href="awskeyinfodefinition.md">AwsKeyInfoDefinition</a></i>
</pre>

## Properties

#### AccountId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreationTime

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CustomerManagedKeyId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseCases

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AwsKeyInfo

_Required_: No

_Type_: List of <a href="awskeyinfodefinition.md">AwsKeyInfoDefinition</a>

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

