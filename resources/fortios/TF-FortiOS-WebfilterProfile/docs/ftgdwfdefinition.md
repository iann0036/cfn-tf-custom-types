# TF::FortiOS::WebfilterProfile FtgdWfDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#exemptquota" title="ExemptQuota">ExemptQuota</a>" : <i>String</i>,
    "<a href="#maxquotatimeout" title="MaxQuotaTimeout">MaxQuotaTimeout</a>" : <i>Double</i>,
    "<a href="#options" title="Options">Options</a>" : <i>String</i>,
    "<a href="#ovrd" title="Ovrd">Ovrd</a>" : <i>String</i>,
    "<a href="#ratecrlurls" title="RateCrlUrls">RateCrlUrls</a>" : <i>String</i>,
    "<a href="#ratecssurls" title="RateCssUrls">RateCssUrls</a>" : <i>String</i>,
    "<a href="#rateimageurls" title="RateImageUrls">RateImageUrls</a>" : <i>String</i>,
    "<a href="#ratejavascripturls" title="RateJavascriptUrls">RateJavascriptUrls</a>" : <i>String</i>,
    "<a href="#filters" title="Filters">Filters</a>" : <i>[ <a href="filtersdefinition.md">FiltersDefinition</a>, ... ]</i>,
    "<a href="#quota" title="Quota">Quota</a>" : <i>[ <a href="quotadefinition.md">QuotaDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#exemptquota" title="ExemptQuota">ExemptQuota</a>: <i>String</i>
<a href="#maxquotatimeout" title="MaxQuotaTimeout">MaxQuotaTimeout</a>: <i>Double</i>
<a href="#options" title="Options">Options</a>: <i>String</i>
<a href="#ovrd" title="Ovrd">Ovrd</a>: <i>String</i>
<a href="#ratecrlurls" title="RateCrlUrls">RateCrlUrls</a>: <i>String</i>
<a href="#ratecssurls" title="RateCssUrls">RateCssUrls</a>: <i>String</i>
<a href="#rateimageurls" title="RateImageUrls">RateImageUrls</a>: <i>String</i>
<a href="#ratejavascripturls" title="RateJavascriptUrls">RateJavascriptUrls</a>: <i>String</i>
<a href="#filters" title="Filters">Filters</a>: <i>
      - <a href="filtersdefinition.md">FiltersDefinition</a></i>
<a href="#quota" title="Quota">Quota</a>: <i>
      - <a href="quotadefinition.md">QuotaDefinition</a></i>
</pre>

## Properties

#### ExemptQuota

Do not stop quota for these categories.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxQuotaTimeout

Maximum FortiGuard quota used by single page view in seconds (excludes streams).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Options

Options for FortiGuard Web Filter. Valid values: `error-allow`, `rate-server-ip`, `connect-request-bypass`, `ftgd-disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ovrd

Allow web filter profile overrides.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateCrlUrls

Enable/disable rating CRL by URL. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateCssUrls

Enable/disable rating CSS by URL. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateImageUrls

Enable/disable rating images by URL. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RateJavascriptUrls

Enable/disable rating JavaScript by URL. Valid values: `disable`, `enable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filters

_Required_: No

_Type_: List of <a href="filtersdefinition.md">FiltersDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quota

_Required_: No

_Type_: List of <a href="quotadefinition.md">QuotaDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

