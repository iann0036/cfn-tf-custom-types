# TF::Metal::SpotMarketRequest InstanceParametersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#alwayspxe" title="AlwaysPxe">AlwaysPxe</a>" : <i>Boolean</i>,
    "<a href="#billingcycle" title="BillingCycle">BillingCycle</a>" : <i>String</i>,
    "<a href="#customdata" title="Customdata">Customdata</a>" : <i>String</i>,
    "<a href="#description" title="Description">Description</a>" : <i>String</i>,
    "<a href="#features" title="Features">Features</a>" : <i>[ String, ... ]</i>,
    "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
    "<a href="#ipxescripturl" title="IpxeScriptUrl">IpxeScriptUrl</a>" : <i>String</i>,
    "<a href="#locked" title="Locked">Locked</a>" : <i>Boolean</i>,
    "<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>" : <i>String</i>,
    "<a href="#plan" title="Plan">Plan</a>" : <i>String</i>,
    "<a href="#projectsshkeys" title="ProjectSshKeys">ProjectSshKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>,
    "<a href="#usersshkeys" title="UserSshKeys">UserSshKeys</a>" : <i>[ String, ... ]</i>,
    "<a href="#userdata" title="Userdata">Userdata</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#alwayspxe" title="AlwaysPxe">AlwaysPxe</a>: <i>Boolean</i>
<a href="#billingcycle" title="BillingCycle">BillingCycle</a>: <i>String</i>
<a href="#customdata" title="Customdata">Customdata</a>: <i>String</i>
<a href="#description" title="Description">Description</a>: <i>String</i>
<a href="#features" title="Features">Features</a>: <i>
      - String</i>
<a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
<a href="#ipxescripturl" title="IpxeScriptUrl">IpxeScriptUrl</a>: <i>String</i>
<a href="#locked" title="Locked">Locked</a>: <i>Boolean</i>
<a href="#operatingsystem" title="OperatingSystem">OperatingSystem</a>: <i>String</i>
<a href="#plan" title="Plan">Plan</a>: <i>String</i>
<a href="#projectsshkeys" title="ProjectSshKeys">ProjectSshKeys</a>: <i>
      - String</i>
<a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
<a href="#usersshkeys" title="UserSshKeys">UserSshKeys</a>: <i>
      - String</i>
<a href="#userdata" title="Userdata">Userdata</a>: <i>String</i>
</pre>

## Properties

#### AlwaysPxe

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BillingCycle

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Customdata

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Features

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IpxeScriptUrl

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locked

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### OperatingSystem

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Plan

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ProjectSshKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserSshKeys

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Userdata

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

