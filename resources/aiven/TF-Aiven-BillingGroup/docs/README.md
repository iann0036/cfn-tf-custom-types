# TF::Aiven::BillingGroup

CloudFormation equivalent of aiven_billing_group

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aiven::BillingGroup",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#addresslines" title="AddressLines">AddressLines</a>" : <i>[ String, ... ]</i>,
        "<a href="#billingcurrency" title="BillingCurrency">BillingCurrency</a>" : <i>String</i>,
        "<a href="#billingemails" title="BillingEmails">BillingEmails</a>" : <i>[ String, ... ]</i>,
        "<a href="#billingextratext" title="BillingExtraText">BillingExtraText</a>" : <i>String</i>,
        "<a href="#cardid" title="CardId">CardId</a>" : <i>String</i>,
        "<a href="#city" title="City">City</a>" : <i>String</i>,
        "<a href="#company" title="Company">Company</a>" : <i>String</i>,
        "<a href="#countrycode" title="CountryCode">CountryCode</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#state" title="State">State</a>" : <i>String</i>,
        "<a href="#vatid" title="VatId">VatId</a>" : <i>String</i>,
        "<a href="#zipcode" title="ZipCode">ZipCode</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aiven::BillingGroup
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#addresslines" title="AddressLines">AddressLines</a>: <i>
      - String</i>
    <a href="#billingcurrency" title="BillingCurrency">BillingCurrency</a>: <i>String</i>
    <a href="#billingemails" title="BillingEmails">BillingEmails</a>: <i>
      - String</i>
    <a href="#billingextratext" title="BillingExtraText">BillingExtraText</a>: <i>String</i>
    <a href="#cardid" title="CardId">CardId</a>: <i>String</i>
    <a href="#city" title="City">City</a>: <i>String</i>
    <a href="#company" title="Company">Company</a>: <i>String</i>
    <a href="#countrycode" title="CountryCode">CountryCode</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#state" title="State">State</a>: <i>String</i>
    <a href="#vatid" title="VatId">VatId</a>: <i>String</i>
    <a href="#zipcode" title="ZipCode">ZipCode</a>: <i>String</i>
</pre>

## Properties

#### AccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AddressLines

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingCurrency

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingEmails

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingExtraText

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CardId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### City

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Company

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CountryCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### State

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VatId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ZipCode

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

#### Id

Returns the <code>Id</code> value.

