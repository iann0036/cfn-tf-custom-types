# TF::Artifactory::XrayPolicy CriteriaDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowunknown" title="AllowUnknown">AllowUnknown</a>" : <i>Boolean</i>,
    "<a href="#allowedlicenses" title="AllowedLicenses">AllowedLicenses</a>" : <i>[ String, ... ]</i>,
    "<a href="#bannedlicenses" title="BannedLicenses">BannedLicenses</a>" : <i>[ String, ... ]</i>,
    "<a href="#minseverity" title="MinSeverity">MinSeverity</a>" : <i>String</i>,
    "<a href="#cvssrange" title="CvssRange">CvssRange</a>" : <i>[ <a href="cvssrangedefinition.md">CvssRangeDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowunknown" title="AllowUnknown">AllowUnknown</a>: <i>Boolean</i>
<a href="#allowedlicenses" title="AllowedLicenses">AllowedLicenses</a>: <i>
      - String</i>
<a href="#bannedlicenses" title="BannedLicenses">BannedLicenses</a>: <i>
      - String</i>
<a href="#minseverity" title="MinSeverity">MinSeverity</a>: <i>String</i>
<a href="#cvssrange" title="CvssRange">CvssRange</a>: <i>
      - <a href="cvssrangedefinition.md">CvssRangeDefinition</a></i>
</pre>

## Properties

#### AllowUnknown

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedLicenses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BannedLicenses

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MinSeverity

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CvssRange

_Required_: No

_Type_: List of <a href="cvssrangedefinition.md">CvssRangeDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

