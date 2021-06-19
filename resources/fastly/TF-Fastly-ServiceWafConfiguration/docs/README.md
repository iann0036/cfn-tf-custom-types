# TF::Fastly::ServiceWafConfiguration

Defines a set of Web Application Firewall configuration options that can be used to populate a service WAF. This resource will configure rules, thresholds and other settings for a WAF.


~> **Warning:** Terraform will take precedence over any changes you make in the UI or API. Such changes are likely to be reversed if you run Terraform again.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Fastly::ServiceWafConfiguration",
    "Properties" : {
        "<a href="#allowedhttpversions" title="AllowedHttpVersions">AllowedHttpVersions</a>" : <i>String</i>,
        "<a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>" : <i>String</i>,
        "<a href="#allowedrequestcontenttype" title="AllowedRequestContentType">AllowedRequestContentType</a>" : <i>String</i>,
        "<a href="#allowedrequestcontenttypecharset" title="AllowedRequestContentTypeCharset">AllowedRequestContentTypeCharset</a>" : <i>String</i>,
        "<a href="#arglength" title="ArgLength">ArgLength</a>" : <i>Double</i>,
        "<a href="#argnamelength" title="ArgNameLength">ArgNameLength</a>" : <i>Double</i>,
        "<a href="#combinedfilesizes" title="CombinedFileSizes">CombinedFileSizes</a>" : <i>Double</i>,
        "<a href="#criticalanomalyscore" title="CriticalAnomalyScore">CriticalAnomalyScore</a>" : <i>Double</i>,
        "<a href="#crsvalidateutf8encoding" title="CrsValidateUtf8Encoding">CrsValidateUtf8Encoding</a>" : <i>Boolean</i>,
        "<a href="#erroranomalyscore" title="ErrorAnomalyScore">ErrorAnomalyScore</a>" : <i>Double</i>,
        "<a href="#highriskcountrycodes" title="HighRiskCountryCodes">HighRiskCountryCodes</a>" : <i>String</i>,
        "<a href="#httpviolationscorethreshold" title="HttpViolationScoreThreshold">HttpViolationScoreThreshold</a>" : <i>Double</i>,
        "<a href="#inboundanomalyscorethreshold" title="InboundAnomalyScoreThreshold">InboundAnomalyScoreThreshold</a>" : <i>Double</i>,
        "<a href="#lfiscorethreshold" title="LfiScoreThreshold">LfiScoreThreshold</a>" : <i>Double</i>,
        "<a href="#maxfilesize" title="MaxFileSize">MaxFileSize</a>" : <i>Double</i>,
        "<a href="#maxnumargs" title="MaxNumArgs">MaxNumArgs</a>" : <i>Double</i>,
        "<a href="#noticeanomalyscore" title="NoticeAnomalyScore">NoticeAnomalyScore</a>" : <i>Double</i>,
        "<a href="#paranoialevel" title="ParanoiaLevel">ParanoiaLevel</a>" : <i>Double</i>,
        "<a href="#phpinjectionscorethreshold" title="PhpInjectionScoreThreshold">PhpInjectionScoreThreshold</a>" : <i>Double</i>,
        "<a href="#rcescorethreshold" title="RceScoreThreshold">RceScoreThreshold</a>" : <i>Double</i>,
        "<a href="#restrictedextensions" title="RestrictedExtensions">RestrictedExtensions</a>" : <i>String</i>,
        "<a href="#restrictedheaders" title="RestrictedHeaders">RestrictedHeaders</a>" : <i>String</i>,
        "<a href="#rfiscorethreshold" title="RfiScoreThreshold">RfiScoreThreshold</a>" : <i>Double</i>,
        "<a href="#sessionfixationscorethreshold" title="SessionFixationScoreThreshold">SessionFixationScoreThreshold</a>" : <i>Double</i>,
        "<a href="#sqlinjectionscorethreshold" title="SqlInjectionScoreThreshold">SqlInjectionScoreThreshold</a>" : <i>Double</i>,
        "<a href="#totalarglength" title="TotalArgLength">TotalArgLength</a>" : <i>Double</i>,
        "<a href="#wafid" title="WafId">WafId</a>" : <i>String</i>,
        "<a href="#warninganomalyscore" title="WarningAnomalyScore">WarningAnomalyScore</a>" : <i>Double</i>,
        "<a href="#xssscorethreshold" title="XssScoreThreshold">XssScoreThreshold</a>" : <i>Double</i>,
        "<a href="#rule" title="Rule">Rule</a>" : <i>[ <a href="ruledefinition.md">RuleDefinition</a>, ... ]</i>,
        "<a href="#ruleexclusion" title="RuleExclusion">RuleExclusion</a>" : <i>[ <a href="ruleexclusiondefinition.md">RuleExclusionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Fastly::ServiceWafConfiguration
Properties:
    <a href="#allowedhttpversions" title="AllowedHttpVersions">AllowedHttpVersions</a>: <i>String</i>
    <a href="#allowedmethods" title="AllowedMethods">AllowedMethods</a>: <i>String</i>
    <a href="#allowedrequestcontenttype" title="AllowedRequestContentType">AllowedRequestContentType</a>: <i>String</i>
    <a href="#allowedrequestcontenttypecharset" title="AllowedRequestContentTypeCharset">AllowedRequestContentTypeCharset</a>: <i>String</i>
    <a href="#arglength" title="ArgLength">ArgLength</a>: <i>Double</i>
    <a href="#argnamelength" title="ArgNameLength">ArgNameLength</a>: <i>Double</i>
    <a href="#combinedfilesizes" title="CombinedFileSizes">CombinedFileSizes</a>: <i>Double</i>
    <a href="#criticalanomalyscore" title="CriticalAnomalyScore">CriticalAnomalyScore</a>: <i>Double</i>
    <a href="#crsvalidateutf8encoding" title="CrsValidateUtf8Encoding">CrsValidateUtf8Encoding</a>: <i>Boolean</i>
    <a href="#erroranomalyscore" title="ErrorAnomalyScore">ErrorAnomalyScore</a>: <i>Double</i>
    <a href="#highriskcountrycodes" title="HighRiskCountryCodes">HighRiskCountryCodes</a>: <i>String</i>
    <a href="#httpviolationscorethreshold" title="HttpViolationScoreThreshold">HttpViolationScoreThreshold</a>: <i>Double</i>
    <a href="#inboundanomalyscorethreshold" title="InboundAnomalyScoreThreshold">InboundAnomalyScoreThreshold</a>: <i>Double</i>
    <a href="#lfiscorethreshold" title="LfiScoreThreshold">LfiScoreThreshold</a>: <i>Double</i>
    <a href="#maxfilesize" title="MaxFileSize">MaxFileSize</a>: <i>Double</i>
    <a href="#maxnumargs" title="MaxNumArgs">MaxNumArgs</a>: <i>Double</i>
    <a href="#noticeanomalyscore" title="NoticeAnomalyScore">NoticeAnomalyScore</a>: <i>Double</i>
    <a href="#paranoialevel" title="ParanoiaLevel">ParanoiaLevel</a>: <i>Double</i>
    <a href="#phpinjectionscorethreshold" title="PhpInjectionScoreThreshold">PhpInjectionScoreThreshold</a>: <i>Double</i>
    <a href="#rcescorethreshold" title="RceScoreThreshold">RceScoreThreshold</a>: <i>Double</i>
    <a href="#restrictedextensions" title="RestrictedExtensions">RestrictedExtensions</a>: <i>String</i>
    <a href="#restrictedheaders" title="RestrictedHeaders">RestrictedHeaders</a>: <i>String</i>
    <a href="#rfiscorethreshold" title="RfiScoreThreshold">RfiScoreThreshold</a>: <i>Double</i>
    <a href="#sessionfixationscorethreshold" title="SessionFixationScoreThreshold">SessionFixationScoreThreshold</a>: <i>Double</i>
    <a href="#sqlinjectionscorethreshold" title="SqlInjectionScoreThreshold">SqlInjectionScoreThreshold</a>: <i>Double</i>
    <a href="#totalarglength" title="TotalArgLength">TotalArgLength</a>: <i>Double</i>
    <a href="#wafid" title="WafId">WafId</a>: <i>String</i>
    <a href="#warninganomalyscore" title="WarningAnomalyScore">WarningAnomalyScore</a>: <i>Double</i>
    <a href="#xssscorethreshold" title="XssScoreThreshold">XssScoreThreshold</a>: <i>Double</i>
    <a href="#rule" title="Rule">Rule</a>: <i>
      - <a href="ruledefinition.md">RuleDefinition</a></i>
    <a href="#ruleexclusion" title="RuleExclusion">RuleExclusion</a>: <i>
      - <a href="ruleexclusiondefinition.md">RuleExclusionDefinition</a></i>
</pre>

## Properties

#### AllowedHttpVersions

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedMethods

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedRequestContentType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AllowedRequestContentTypeCharset

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArgLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ArgNameLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CombinedFileSizes

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CriticalAnomalyScore

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrsValidateUtf8Encoding

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ErrorAnomalyScore

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HighRiskCountryCodes

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpViolationScoreThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InboundAnomalyScoreThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LfiScoreThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxFileSize

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxNumArgs

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoticeAnomalyScore

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ParanoiaLevel

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PhpInjectionScoreThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RceScoreThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedExtensions

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedHeaders

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RfiScoreThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SessionFixationScoreThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SqlInjectionScoreThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TotalArgLength

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WafId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WarningAnomalyScore

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### XssScoreThreshold

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Rule

_Required_: No

_Type_: List of <a href="ruledefinition.md">RuleDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RuleExclusion

_Required_: No

_Type_: List of <a href="ruleexclusiondefinition.md">RuleExclusionDefinition</a>

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

