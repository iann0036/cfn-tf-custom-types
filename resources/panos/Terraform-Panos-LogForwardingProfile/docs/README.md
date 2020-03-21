# Terraform::Panos::LogForwardingProfile

CloudFormation equivalent of panos_log_forwarding_profile

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Panos::LogForwardingProfile",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#enhancedlogging" title="EnhancedLogging">EnhancedLogging</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vsys" title="Vsys">Vsys</a>" : <i>String</i>,
        "<a href="#matchlist" title="MatchList">MatchList</a>" : <i>[ &lt;a href=&#34;matchlist.md&#34;&gt;MatchList&lt;/a&gt;, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
        "<a href="#azureintegration" title="AzureIntegration">AzureIntegration</a>" : <i>[ &lt;a href=&#34;azureintegration.md&#34;&gt;AzureIntegration&lt;/a&gt;, ... ]</i>,
        "<a href="#taggingintegration" title="TaggingIntegration">TaggingIntegration</a>" : <i>[ &lt;a href=&#34;taggingintegration.md&#34;&gt;TaggingIntegration&lt;/a&gt;, ... ]</i>,
        "<a href="#localregistration" title="LocalRegistration">LocalRegistration</a>" : <i>[ &lt;a href=&#34;localregistration.md&#34;&gt;LocalRegistration&lt;/a&gt;, ... ]</i>,
        "<a href="#panoramaregistration" title="PanoramaRegistration">PanoramaRegistration</a>" : <i>[ &lt;a href=&#34;panoramaregistration.md&#34;&gt;PanoramaRegistration&lt;/a&gt;, ... ]</i>,
        "<a href="#remoteregistration" title="RemoteRegistration">RemoteRegistration</a>" : <i>[ &lt;a href=&#34;remoteregistration.md&#34;&gt;RemoteRegistration&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Panos::LogForwardingProfile
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#enhancedlogging" title="EnhancedLogging">EnhancedLogging</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vsys" title="Vsys">Vsys</a>: <i>String</i>
    <a href="#matchlist" title="MatchList">MatchList</a>: <i>
      - &lt;a href=&#34;matchlist.md&#34;&gt;MatchList&lt;/a&gt;</i>
    <a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;</i>
    <a href="#azureintegration" title="AzureIntegration">AzureIntegration</a>: <i>
      - &lt;a href=&#34;azureintegration.md&#34;&gt;AzureIntegration&lt;/a&gt;</i>
    <a href="#taggingintegration" title="TaggingIntegration">TaggingIntegration</a>: <i>
      - &lt;a href=&#34;taggingintegration.md&#34;&gt;TaggingIntegration&lt;/a&gt;</i>
    <a href="#localregistration" title="LocalRegistration">LocalRegistration</a>: <i>
      - &lt;a href=&#34;localregistration.md&#34;&gt;LocalRegistration&lt;/a&gt;</i>
    <a href="#panoramaregistration" title="PanoramaRegistration">PanoramaRegistration</a>: <i>
      - &lt;a href=&#34;panoramaregistration.md&#34;&gt;PanoramaRegistration&lt;/a&gt;</i>
    <a href="#remoteregistration" title="RemoteRegistration">RemoteRegistration</a>: <i>
      - &lt;a href=&#34;remoteregistration.md&#34;&gt;RemoteRegistration&lt;/a&gt;</i>
</pre>

## Properties

#### Description

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnhancedLogging

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vsys

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MatchList

_Required_: No

_Type_: List of &lt;a href=&#34;matchlist.md&#34;&gt;MatchList&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AzureIntegration

_Required_: No

_Type_: List of &lt;a href=&#34;azureintegration.md&#34;&gt;AzureIntegration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TaggingIntegration

_Required_: No

_Type_: List of &lt;a href=&#34;taggingintegration.md&#34;&gt;TaggingIntegration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LocalRegistration

_Required_: No

_Type_: List of &lt;a href=&#34;localregistration.md&#34;&gt;LocalRegistration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PanoramaRegistration

_Required_: No

_Type_: List of &lt;a href=&#34;panoramaregistration.md&#34;&gt;PanoramaRegistration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RemoteRegistration

_Required_: No

_Type_: List of &lt;a href=&#34;remoteregistration.md&#34;&gt;RemoteRegistration&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

