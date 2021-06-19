# TF::Aiven::Project

CloudFormation equivalent of aiven_project

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aiven::Project",
    "Properties" : {
        "<a href="#accountid" title="AccountId">AccountId</a>" : <i>String</i>,
        "<a href="#availablecredits" title="AvailableCredits">AvailableCredits</a>" : <i>String</i>,
        "<a href="#billingaddress" title="BillingAddress">BillingAddress</a>" : <i>String</i>,
        "<a href="#billingcurrency" title="BillingCurrency">BillingCurrency</a>" : <i>String</i>,
        "<a href="#billingemails" title="BillingEmails">BillingEmails</a>" : <i>[ String, ... ]</i>,
        "<a href="#billingextratext" title="BillingExtraText">BillingExtraText</a>" : <i>String</i>,
        "<a href="#billinggroup" title="BillingGroup">BillingGroup</a>" : <i>String</i>,
        "<a href="#cacert" title="CaCert">CaCert</a>" : <i>String</i>,
        "<a href="#cardid" title="CardId">CardId</a>" : <i>String</i>,
        "<a href="#copyfromproject" title="CopyFromProject">CopyFromProject</a>" : <i>String</i>,
        "<a href="#countrycode" title="CountryCode">CountryCode</a>" : <i>String</i>,
        "<a href="#defaultcloud" title="DefaultCloud">DefaultCloud</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#technicalemails" title="TechnicalEmails">TechnicalEmails</a>" : <i>[ String, ... ]</i>,
        "<a href="#vatid" title="VatId">VatId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aiven::Project
Properties:
    <a href="#accountid" title="AccountId">AccountId</a>: <i>String</i>
    <a href="#availablecredits" title="AvailableCredits">AvailableCredits</a>: <i>String</i>
    <a href="#billingaddress" title="BillingAddress">BillingAddress</a>: <i>String</i>
    <a href="#billingcurrency" title="BillingCurrency">BillingCurrency</a>: <i>String</i>
    <a href="#billingemails" title="BillingEmails">BillingEmails</a>: <i>
      - String</i>
    <a href="#billingextratext" title="BillingExtraText">BillingExtraText</a>: <i>String</i>
    <a href="#billinggroup" title="BillingGroup">BillingGroup</a>: <i>String</i>
    <a href="#cacert" title="CaCert">CaCert</a>: <i>String</i>
    <a href="#cardid" title="CardId">CardId</a>: <i>String</i>
    <a href="#copyfromproject" title="CopyFromProject">CopyFromProject</a>: <i>String</i>
    <a href="#countrycode" title="CountryCode">CountryCode</a>: <i>String</i>
    <a href="#defaultcloud" title="DefaultCloud">DefaultCloud</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#technicalemails" title="TechnicalEmails">TechnicalEmails</a>: <i>
      - String</i>
    <a href="#vatid" title="VatId">VatId</a>: <i>String</i>
</pre>

## Properties

#### AccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AvailableCredits

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingAddress

_Required_: No

_Type_: String

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

#### BillingGroup

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CaCert

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CardId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CopyFromProject

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CountryCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultCloud

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TechnicalEmails

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VatId

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

#### Country

Returns the <code>Country</code> value.

#### EstimatedBalance

Returns the <code>EstimatedBalance</code> value.

#### Id

Returns the <code>Id</code> value.

#### PaymentMethod

Returns the <code>PaymentMethod</code> value.

