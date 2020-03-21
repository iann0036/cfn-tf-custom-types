# Terraform::OpenTelekomCloud::WafPolicyV1 Options

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#antitamper" title="Antitamper">Antitamper</a>" : <i>Boolean</i>,
    "<a href="#cc" title="Cc">Cc</a>" : <i>Boolean</i>,
    "<a href="#common" title="Common">Common</a>" : <i>Boolean</i>,
    "<a href="#crawler" title="Crawler">Crawler</a>" : <i>Boolean</i>,
    "<a href="#crawlerengine" title="CrawlerEngine">CrawlerEngine</a>" : <i>Boolean</i>,
    "<a href="#crawlerother" title="CrawlerOther">CrawlerOther</a>" : <i>Boolean</i>,
    "<a href="#crawlerscanner" title="CrawlerScanner">CrawlerScanner</a>" : <i>Boolean</i>,
    "<a href="#crawlerscript" title="CrawlerScript">CrawlerScript</a>" : <i>Boolean</i>,
    "<a href="#custom" title="Custom">Custom</a>" : <i>Boolean</i>,
    "<a href="#ignore" title="Ignore">Ignore</a>" : <i>Boolean</i>,
    "<a href="#privacy" title="Privacy">Privacy</a>" : <i>Boolean</i>,
    "<a href="#webattack" title="Webattack">Webattack</a>" : <i>Boolean</i>,
    "<a href="#webshell" title="Webshell">Webshell</a>" : <i>Boolean</i>,
    "<a href="#whiteblackip" title="Whiteblackip">Whiteblackip</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#antitamper" title="Antitamper">Antitamper</a>: <i>Boolean</i>
<a href="#cc" title="Cc">Cc</a>: <i>Boolean</i>
<a href="#common" title="Common">Common</a>: <i>Boolean</i>
<a href="#crawler" title="Crawler">Crawler</a>: <i>Boolean</i>
<a href="#crawlerengine" title="CrawlerEngine">CrawlerEngine</a>: <i>Boolean</i>
<a href="#crawlerother" title="CrawlerOther">CrawlerOther</a>: <i>Boolean</i>
<a href="#crawlerscanner" title="CrawlerScanner">CrawlerScanner</a>: <i>Boolean</i>
<a href="#crawlerscript" title="CrawlerScript">CrawlerScript</a>: <i>Boolean</i>
<a href="#custom" title="Custom">Custom</a>: <i>Boolean</i>
<a href="#ignore" title="Ignore">Ignore</a>: <i>Boolean</i>
<a href="#privacy" title="Privacy">Privacy</a>: <i>Boolean</i>
<a href="#webattack" title="Webattack">Webattack</a>: <i>Boolean</i>
<a href="#webshell" title="Webshell">Webshell</a>: <i>Boolean</i>
<a href="#whiteblackip" title="Whiteblackip">Whiteblackip</a>: <i>Boolean</i>
</pre>

## Properties

#### Antitamper

Specifies whether Web Tamper Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cc

Specifies whether CC Attack Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Common

Specifies whether General Check in Basic Web Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Crawler

Specifies whether the master crawler detection switch in Basic Web Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrawlerEngine

Specifies whether the Search Engine switch in Basic Web Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrawlerOther

Specifies whether detection of other crawlers in Basic Web Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrawlerScanner

Specifies whether the Scanner switch in Basic Web Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrawlerScript

Specifies whether the Script Tool switch in Basic Web Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Custom

Specifies whether Precise Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ignore

Specifies whether False Alarm Masking is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Privacy

Specifies whether Data Masking is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webattack

Specifies whether Basic Web Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Webshell

Specifies whether webshell detection in Basic Web Protection is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Whiteblackip

Specifies whether Blacklist and Whitelist is enabled.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

