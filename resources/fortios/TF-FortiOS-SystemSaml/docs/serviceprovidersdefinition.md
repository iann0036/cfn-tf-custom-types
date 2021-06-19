# TF::FortiOS::SystemSaml ServiceProvidersDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>" : <i>String</i>,
    "<a href="#idpsinglelogouturl" title="IdpSingleLogoutUrl">IdpSingleLogoutUrl</a>" : <i>String</i>,
    "<a href="#idpsinglesignonurl" title="IdpSingleSignOnUrl">IdpSingleSignOnUrl</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#prefix" title="Prefix">Prefix</a>" : <i>String</i>,
    "<a href="#spcert" title="SpCert">SpCert</a>" : <i>String</i>,
    "<a href="#spentityid" title="SpEntityId">SpEntityId</a>" : <i>String</i>,
    "<a href="#spportalurl" title="SpPortalUrl">SpPortalUrl</a>" : <i>String</i>,
    "<a href="#spsinglelogouturl" title="SpSingleLogoutUrl">SpSingleLogoutUrl</a>" : <i>String</i>,
    "<a href="#spsinglesignonurl" title="SpSingleSignOnUrl">SpSingleSignOnUrl</a>" : <i>String</i>,
    "<a href="#assertionattributes" title="AssertionAttributes">AssertionAttributes</a>" : <i>[ <a href="assertionattributesdefinition.md">AssertionAttributesDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#idpentityid" title="IdpEntityId">IdpEntityId</a>: <i>String</i>
<a href="#idpsinglelogouturl" title="IdpSingleLogoutUrl">IdpSingleLogoutUrl</a>: <i>String</i>
<a href="#idpsinglesignonurl" title="IdpSingleSignOnUrl">IdpSingleSignOnUrl</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#prefix" title="Prefix">Prefix</a>: <i>String</i>
<a href="#spcert" title="SpCert">SpCert</a>: <i>String</i>
<a href="#spentityid" title="SpEntityId">SpEntityId</a>: <i>String</i>
<a href="#spportalurl" title="SpPortalUrl">SpPortalUrl</a>: <i>String</i>
<a href="#spsinglelogouturl" title="SpSingleLogoutUrl">SpSingleLogoutUrl</a>: <i>String</i>
<a href="#spsinglesignonurl" title="SpSingleSignOnUrl">SpSingleSignOnUrl</a>: <i>String</i>
<a href="#assertionattributes" title="AssertionAttributes">AssertionAttributes</a>: <i>
      - <a href="assertionattributesdefinition.md">AssertionAttributesDefinition</a></i>
</pre>

## Properties

#### IdpEntityId

IDP entity ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpSingleLogoutUrl

IDP single logout URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IdpSingleSignOnUrl

IDP single sign-on URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Prefix

Prefix.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpCert

SP certificate name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpEntityId

SP entity ID.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpPortalUrl

SP portal URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpSingleLogoutUrl

SP single logout URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpSingleSignOnUrl

SP single sign-on URL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssertionAttributes

_Required_: No

_Type_: List of <a href="assertionattributesdefinition.md">AssertionAttributesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

