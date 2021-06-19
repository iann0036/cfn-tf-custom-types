# TF::Google::CloudAssetOrganizationFeed

Describes a Cloud Asset Inventory feed used to to listen to asset updates.


To get more information about OrganizationFeed, see:

* [API documentation](https://cloud.google.com/asset-inventory/docs/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/asset-inventory/docs)

<div class = "oics-button" style="float: right; margin: 0 0 -15px">
  <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=cloud_asset_organization_feed&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
    <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
  </a>
</div>

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::CloudAssetOrganizationFeed",
    "Properties" : {
        "<a href="#assetnames" title="AssetNames">AssetNames</a>" : <i>[ String, ... ]</i>,
        "<a href="#assettypes" title="AssetTypes">AssetTypes</a>" : <i>[ String, ... ]</i>,
        "<a href="#billingproject" title="BillingProject">BillingProject</a>" : <i>String</i>,
        "<a href="#contenttype" title="ContentType">ContentType</a>" : <i>String</i>,
        "<a href="#feedid" title="FeedId">FeedId</a>" : <i>String</i>,
        "<a href="#orgid" title="OrgId">OrgId</a>" : <i>String</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ <a href="conditiondefinition.md">ConditionDefinition</a>, ... ]</i>,
        "<a href="#feedoutputconfig" title="FeedOutputConfig">FeedOutputConfig</a>" : <i>[ <a href="feedoutputconfigdefinition.md">FeedOutputConfigDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::CloudAssetOrganizationFeed
Properties:
    <a href="#assetnames" title="AssetNames">AssetNames</a>: <i>
      - String</i>
    <a href="#assettypes" title="AssetTypes">AssetTypes</a>: <i>
      - String</i>
    <a href="#billingproject" title="BillingProject">BillingProject</a>: <i>String</i>
    <a href="#contenttype" title="ContentType">ContentType</a>: <i>String</i>
    <a href="#feedid" title="FeedId">FeedId</a>: <i>String</i>
    <a href="#orgid" title="OrgId">OrgId</a>: <i>String</i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - <a href="conditiondefinition.md">ConditionDefinition</a></i>
    <a href="#feedoutputconfig" title="FeedOutputConfig">FeedOutputConfig</a>: <i>
      - <a href="feedoutputconfigdefinition.md">FeedOutputConfigDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AssetNames

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssetTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingProject

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeedId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OrgId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of <a href="conditiondefinition.md">ConditionDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FeedOutputConfig

_Required_: No

_Type_: List of <a href="feedoutputconfigdefinition.md">FeedOutputConfigDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Name

Returns the <code>Name</code> value.

