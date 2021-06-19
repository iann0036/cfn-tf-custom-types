# TF::OCI::WaasWaasPolicy ProtectionSettingsDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowedhttpmethods" title="AllowedHttpMethods">AllowedHttpMethods</a>" : <i>[ String, ... ]</i>,
    "<a href="#blockaction" title="BlockAction">BlockAction</a>" : <i>String</i>,
    "<a href="#blockerrorpagecode" title="BlockErrorPageCode">BlockErrorPageCode</a>" : <i>String</i>,
    "<a href="#blockerrorpagedescription" title="BlockErrorPageDescription">BlockErrorPageDescription</a>" : <i>String</i>,
    "<a href="#blockerrorpagemessage" title="BlockErrorPageMessage">BlockErrorPageMessage</a>" : <i>String</i>,
    "<a href="#blockresponsecode" title="BlockResponseCode">BlockResponseCode</a>" : <i>Double</i>,
    "<a href="#isresponseinspected" title="IsResponseInspected">IsResponseInspected</a>" : <i>Boolean</i>,
    "<a href="#maxargumentcount" title="MaxArgumentCount">MaxArgumentCount</a>" : <i>Double</i>,
    "<a href="#maxnamelengthperargument" title="MaxNameLengthPerArgument">MaxNameLengthPerArgument</a>" : <i>Double</i>,
    "<a href="#maxresponsesizeinkib" title="MaxResponseSizeInKiB">MaxResponseSizeInKiB</a>" : <i>Double</i>,
    "<a href="#maxtotalnamelengthofarguments" title="MaxTotalNameLengthOfArguments">MaxTotalNameLengthOfArguments</a>" : <i>Double</i>,
    "<a href="#mediatypes" title="MediaTypes">MediaTypes</a>" : <i>[ String, ... ]</i>,
    "<a href="#recommendationsperiodindays" title="RecommendationsPeriodInDays">RecommendationsPeriodInDays</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#allowedhttpmethods" title="AllowedHttpMethods">AllowedHttpMethods</a>: <i>
      - String</i>
<a href="#blockaction" title="BlockAction">BlockAction</a>: <i>String</i>
<a href="#blockerrorpagecode" title="BlockErrorPageCode">BlockErrorPageCode</a>: <i>String</i>
<a href="#blockerrorpagedescription" title="BlockErrorPageDescription">BlockErrorPageDescription</a>: <i>String</i>
<a href="#blockerrorpagemessage" title="BlockErrorPageMessage">BlockErrorPageMessage</a>: <i>String</i>
<a href="#blockresponsecode" title="BlockResponseCode">BlockResponseCode</a>: <i>Double</i>
<a href="#isresponseinspected" title="IsResponseInspected">IsResponseInspected</a>: <i>Boolean</i>
<a href="#maxargumentcount" title="MaxArgumentCount">MaxArgumentCount</a>: <i>Double</i>
<a href="#maxnamelengthperargument" title="MaxNameLengthPerArgument">MaxNameLengthPerArgument</a>: <i>Double</i>
<a href="#maxresponsesizeinkib" title="MaxResponseSizeInKiB">MaxResponseSizeInKiB</a>: <i>Double</i>
<a href="#maxtotalnamelengthofarguments" title="MaxTotalNameLengthOfArguments">MaxTotalNameLengthOfArguments</a>: <i>Double</i>
<a href="#mediatypes" title="MediaTypes">MediaTypes</a>: <i>
      - String</i>
<a href="#recommendationsperiodindays" title="RecommendationsPeriodInDays">RecommendationsPeriodInDays</a>: <i>Double</i>
</pre>

## Properties

#### AllowedHttpMethods

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockAction

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockErrorPageCode

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockErrorPageDescription

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockErrorPageMessage

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BlockResponseCode

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsResponseInspected

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxArgumentCount

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNameLengthPerArgument

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxResponseSizeInKiB

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTotalNameLengthOfArguments

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MediaTypes

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RecommendationsPeriodInDays

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

