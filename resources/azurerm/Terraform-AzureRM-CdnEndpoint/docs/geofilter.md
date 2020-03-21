# Terraform::AzureRM::CdnEndpoint GeoFilter

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#action" title="Action">Action</a>" : <i>String</i>,
    "<a href="#countrycodes" title="CountryCodes">CountryCodes</a>" : <i>[ String, ... ]</i>,
    "<a href="#relativepath" title="RelativePath">RelativePath</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#action" title="Action">Action</a>: <i>String</i>
<a href="#countrycodes" title="CountryCodes">CountryCodes</a>: <i>
      - String</i>
<a href="#relativepath" title="RelativePath">RelativePath</a>: <i>String</i>
</pre>

## Properties

#### Action

The Action of the Geo Filter. Possible values include `Allow` and `Block`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CountryCodes

A List of two letter country codes (e.g. `US`, `GB`) to be associated with this Geo Filter.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RelativePath

The relative path applicable to geo filter.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

