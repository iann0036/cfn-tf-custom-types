# TF::FortiOS::WebfilterProfile WebDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#allowlist" title="Allowlist">Allowlist</a>" : <i>String</i>,
    "<a href="#blacklist" title="Blacklist">Blacklist</a>" : <i>String</i>,
    "<a href="#blocklist" title="Blocklist">Blocklist</a>" : <i>String</i>,
    "<a href="#bwordtable" title="BwordTable">BwordTable</a>" : <i>Double</i>,
    "<a href="#bwordthreshold" title="BwordThreshold">BwordThreshold</a>" : <i>Double</i>,
    "<a href="#contentheaderlist" title="ContentHeaderList">ContentHeaderList</a>" : <i>Double</i>,
    "<a href="#logsearch" title="LogSearch">LogSearch</a>" : <i>String</i>,
    "<a href="#safesearch" title="SafeSearch">SafeSearch</a>" : <i>String</i>,
    "<a href="#urlfiltertable" title="UrlfilterTable">UrlfilterTable</a>" : <i>Double</i>,
    "<a href="#whitelist" title="Whitelist">Whitelist</a>" : <i>String</i>,
    "<a href="#youtuberestrict" title="YoutubeRestrict">YoutubeRestrict</a>" : <i>String</i>,
    "<a href="#keywordmatch" title="KeywordMatch">KeywordMatch</a>" : <i>[ <a href="keywordmatchdefinition.md">KeywordMatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#allowlist" title="Allowlist">Allowlist</a>: <i>String</i>
<a href="#blacklist" title="Blacklist">Blacklist</a>: <i>String</i>
<a href="#blocklist" title="Blocklist">Blocklist</a>: <i>String</i>
<a href="#bwordtable" title="BwordTable">BwordTable</a>: <i>Double</i>
<a href="#bwordthreshold" title="BwordThreshold">BwordThreshold</a>: <i>Double</i>
<a href="#contentheaderlist" title="ContentHeaderList">ContentHeaderList</a>: <i>Double</i>
<a href="#logsearch" title="LogSearch">LogSearch</a>: <i>String</i>
<a href="#safesearch" title="SafeSearch">SafeSearch</a>: <i>String</i>
<a href="#urlfiltertable" title="UrlfilterTable">UrlfilterTable</a>: <i>Double</i>
<a href="#whitelist" title="Whitelist">Whitelist</a>: <i>String</i>
<a href="#youtuberestrict" title="YoutubeRestrict">YoutubeRestrict</a>: <i>String</i>
<a href="#keywordmatch" title="KeywordMatch">KeywordMatch</a>: <i>
      - <a href="keywordmatchdefinition.md">KeywordMatchDefinition</a></i>
</pre>

## Properties

#### Allowlist

FortiGuard allowlist settings. Valid values: `exempt-av`, `exempt-webcontent`, `exempt-activex-java-cookie`, `exempt-dlp`, `exempt-rangeblock`, `extended-log-others`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Blacklist

Enable/disable automatic addition of URLs detected by FortiSandbox to blacklist. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Blocklist

Enable/disable automatic addition of URLs detected by FortiSandbox to blocklist. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwordTable

Banned word table ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BwordThreshold

Banned word score threshold.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ContentHeaderList

Content header list.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LogSearch

Enable/disable logging all search phrases. Valid values: `enable`, `disable`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SafeSearch

Safe search type. Valid values: `url`, `header`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UrlfilterTable

URL filter table ID.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whitelist

FortiGuard whitelist settings. Valid values: `exempt-av`, `exempt-webcontent`, `exempt-activex-java-cookie`, `exempt-dlp`, `exempt-rangeblock`, `extended-log-others`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### YoutubeRestrict

YouTube EDU filter level. Valid values: `none`, `strict`, `moderate`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KeywordMatch

_Required_: No

_Type_: List of <a href="keywordmatchdefinition.md">KeywordMatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

