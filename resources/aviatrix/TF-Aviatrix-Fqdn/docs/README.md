# TF::Aviatrix::Fqdn

The **aviatrix_fqdn** resource manages [FQDN filtering](https://docs.aviatrix.com/HowTos/fqdn_faq.html) for Aviatrix gateways.

~> **NOTE on FQDN and FQDN Tag Rule resources:** Terraform currently provides both a standalone FQDN Tag Rule resource and an FQDN resource with domain name rules defined in-line. At this time, you cannot use an FQDN resource with in-line rules in conjunction with any FQDN Tag Rule resources. Doing so will cause a conflict of rule settings and will overwrite rules. In order to use the **aviatrix_fqdn_tag_rule** resource, `manage_domain_names` must be set to false in this resource.

~> **NOTE:** Please see the [Notes](#notes) section below for troubleshooting known issues/deltas that may occur when enabling this feature

~> **NOTE:** Please note that there is no need to attach FQDN resource/enable this feature for the HA gateway. Enabling FQDN for the primary gateway will automatically handle this for the HA

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::Fqdn",
    "Properties" : {
        "<a href="#fqdnenabled" title="FqdnEnabled">FqdnEnabled</a>" : <i>Boolean</i>,
        "<a href="#fqdnmode" title="FqdnMode">FqdnMode</a>" : <i>String</i>,
        "<a href="#fqdntag" title="FqdnTag">FqdnTag</a>" : <i>String</i>,
        "<a href="#managedomainnames" title="ManageDomainNames">ManageDomainNames</a>" : <i>Boolean</i>,
        "<a href="#domainnames" title="DomainNames">DomainNames</a>" : <i>[ <a href="domainnamesdefinition.md">DomainNamesDefinition</a>, ... ]</i>,
        "<a href="#gwfiltertaglist" title="GwFilterTagList">GwFilterTagList</a>" : <i>[ <a href="gwfiltertaglistdefinition.md">GwFilterTagListDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::Fqdn
Properties:
    <a href="#fqdnenabled" title="FqdnEnabled">FqdnEnabled</a>: <i>Boolean</i>
    <a href="#fqdnmode" title="FqdnMode">FqdnMode</a>: <i>String</i>
    <a href="#fqdntag" title="FqdnTag">FqdnTag</a>: <i>String</i>
    <a href="#managedomainnames" title="ManageDomainNames">ManageDomainNames</a>: <i>Boolean</i>
    <a href="#domainnames" title="DomainNames">DomainNames</a>: <i>
      - <a href="domainnamesdefinition.md">DomainNamesDefinition</a></i>
    <a href="#gwfiltertaglist" title="GwFilterTagList">GwFilterTagList</a>: <i>
      - <a href="gwfiltertaglistdefinition.md">GwFilterTagListDefinition</a></i>
</pre>

## Properties

#### FqdnEnabled

FQDN Filter tag status. Valid values: true, false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FqdnMode

Specify FQDN mode: whitelist or blacklist. Valid values: "white", "black".

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FqdnTag

FQDN Filter tag name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ManageDomainNames

Enable to manage domain name rules in-line. If false, domain name rules must be managed using `aviatrix_fqdn_tag_rule` resources. Default: true. Valid values: true, false. Available in provider version R2.17+.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainNames

_Required_: No

_Type_: List of <a href="domainnamesdefinition.md">DomainNamesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GwFilterTagList

_Required_: No

_Type_: List of <a href="gwfiltertaglistdefinition.md">GwFilterTagListDefinition</a>

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

